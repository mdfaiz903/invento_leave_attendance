# HR Leave & Attendance Module

A simple **custom Frappe app** for managing Leave Requests and Attendance approvals.  
Built with **Frappe Framework v16 (dev)**.  

Repository: [invento_leave_attendance](https://github.com/mdfaiz903/invento_leave_attendance)  
(Current branch: `develop`)
(Production branch: `main`)

---

## 🛠️ Installation

### 1. Setup Frappe Bench (v16 dev)
```bash
# Install bench if not already installed
pip install frappe-bench

# Init bench with frappe v16
bench init frappe-bench --frappe-branch version-16
cd frappe-bench

# Create site
bench new-site site_name
2. Get the App
cd apps
git clone https://github.com/mdfaiz903/invento_leave_attendance.git
cd ..
3. Install on Site
bench --site site_name install-app invento_leave_attendance
bench start


# Features & Functionality
📌 Leave Request Doctype
Employee (linked to ERPNext Employee Doc)

From Date / To Date validation

Leave Type (CL, SL, EL)

Status workflow: Pending → Approved / Rejected

Approved By (auto-filled when approved)

Total Days (auto-calculated excluding weekends)

📌 Server-side validations
From Date must be before To Date

Maximum leave duration: 5 days

📌 Client-side logic
Auto-calculate Total Days excluding Saturday & Sunday

Show info message when Leave Type = EL

Custom Approve button

Visible only to HR Manager when status = Pending

Sets Status = Approved and Approved By = current user

📌 Script Report: Leave Summary by Employee
Employee

Total Leave Requests

Approved Leaves

Rejected Leaves

Grouped by Employee

📷 Screenshots
Leave Request Doc
<img src="Screenshot/Leave_request_doc.png" alt="Leave Request Doc" />

Approved
<img src="Screenshot/approved.png" alt="Leave Request Doc Approved" />

Rejected
<img src="Screenshot/rejected.png" alt="Leave Request Doc Rejected" />

Pending
<img src="Screenshot/pending.png" alt="Leave Request Doc Pending" />

Earned Leave Message
<img src="Screenshot/EL_Message_throw.png" alt="Leave Request Doc Earn Leave msg" />

Leave Summary Report
<img src="Screenshot/leave_summary_report.png" alt="Leave Summary Report" />

Print View of Report
<img src="Screenshot/print_view.png" alt="Print View of Report" />


