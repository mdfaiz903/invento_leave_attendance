// Copyright (c) 2025, faiz and contributors
// For license information, please see license.txt

frappe.ui.form.on("Leave Request", {
	refresh(frm) {
        if(frm.doc.status === "Pending")
        frm.add_custom_button(__("Approve"),function(){
            frm.set_value("status","Approved")
            frm.set_value("approved_by",frappe.session.user)
            frm.save()
        })
	},
});
