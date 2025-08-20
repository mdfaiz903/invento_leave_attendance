# Copyright (c) 2025, faiz and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Employee"),
			"fieldname": "employee",
			"fieldtype": "Link",
			"options":"Employee"
		},
		{
			"label": _("Total Leave Requests"),
			"fieldname": "total_lev_req",
			"fieldtype": "Int",
		},
		{
			"label": _("Approved Leaves"),
			"fieldname": "approved_leaves",
			"fieldtype": "Int",
		},
		{
			"label": _("Rejected Leaves"),
			"fieldname": "rejected_leaves",
			"fieldtype": "Int",
		},
		
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	
	records = frappe.db.sql("""
				SELECT
					employee,
					COUNT(*) AS total_lev_req,
					SUM(CASE WHEN status = 'Approved' THEN 1 ELSE 0 END) AS approved_leaves,
					SUM(CASE WHEN status = 'Rejected' THEN 1 ELSE 0 END) AS rejected_leaves
				FROM `tabLeave Request`
				GROUP BY employee
				ORDER BY employee
					
				""",as_dict=True)
	return records
