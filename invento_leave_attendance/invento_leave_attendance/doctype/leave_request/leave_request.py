# Copyright (c) 2025, faiz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate,date_diff


class LeaveRequest(Document):
	def validate(self):
		self.validate_leave_dates()
  
	def validate_leave_dates(self):
		if not self.from_date and self.to_date: return
		from_date = getdate(self.from_date)
		to_date = getdate(self.to_date)
  
		if from_date > to_date:
			frappe.throw("<b>From Date</b> is earlier than the <b>To Date</b>")
		
		leave_date_diff = date_diff(to_date,from_date) + 1
		if leave_date_diff > 5:
			frappe.throw("From Date and To Date, must not <b>exceed 5 days</b>")
   

      
	  
	  

		
	 
