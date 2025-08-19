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
    leave_type:function(frm){
        if(frm.doc.leave_type==="EL"){
            frappe.msgprint("<b>Earned Leave requires manager approval.</b>")
        }
    },
    from_date:function(frm){
        calculate_total_days(frm)
        
    },
    to_date:function(frm){
        calculate_total_days(frm)

    }
});
function calculate_total_days(frm){
    const from_date = frm.doc.from_date 
    const to_date = frm.doc.to_date

    console.log("########",from_date);
    const start = frappe.datetime.str_to_obj(from_date)
    const end = frappe.datetime.str_to_obj(to_date)
    const current = new Date(start.getTime())
    let total_days = frappe.datetime.get_day_diff(to_date, from_date)+1;
    let weekend_days = 0;
    for (current; current <= end; current.setDate(current.getDate() + 1)) {
        let day = current.getDay();
        if (day === 0 || day === 6) { // 0 is Sunday, 6 is Saturday
            weekend_days++;
        }
    }

    let working_days = total_days - weekend_days;
    frm.set_value('total_days', working_days);
    

}
