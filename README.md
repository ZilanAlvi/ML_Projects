# =======================================
# EXTRA WORK API DOCUMENTATION
# =======================================


# Extra Work Inbox Page

## Overview
Renders the Extra Work Inbox HTML page for the Super Admin.
Accessible only by super admins or designated approvers.

---

## HTTP Method

`GET`

---

## API URL

```
{{BASE_URL}}/super_admin/extra_work/inbox
```

---

## cURL Example

```bash
curl --location 'http://localhost:9000/super_admin/extra_work/inbox' \
--header 'Cookie: access_token=<SESSION_TOKEN>'
```

---

## Success Response

Status Code: `200 OK`

Returns HTML page (sh_extra_work_inbox.html).
Page data is loaded separately via /inbox/data endpoint.

---

## Error Response

Status Code: `403 Forbidden`

Returns unauthorized.html with message:
"You don't have access to Extra Work Inbox."


================================================================================


# Extra Work Inbox Data

## Overview
Fetches paginated list of extra work requests with stats, employee info, and approval status.
Used by the inbox page to load data via JavaScript.

---

## HTTP Method

`GET`

---

## API URL

```
{{BASE_URL}}/super_admin/extra_work/inbox/data
```

---

## cURL Example

```bash
curl --location 'http://localhost:9000/super_admin/extra_work/inbox/data?page=1&limit=50&status=PENDING&q=john' \
--header 'Cookie: access_token=<SESSION_TOKEN>'
```

---

## Query Parameters

| Field  | Type    | Required | Description                                 |
|--------|---------|----------|---------------------------------------------|
| q      | string  | No       | Search by employee name, code, or username  |
| status | string  | No       | Filter by status: PENDING, APPROVED, REJECTED |
| page   | integer | No       | Page number (default: 1)                    |
| limit  | integer | No       | Records per page (default: 50)              |

---

## Success Response

Status Code: `200 OK`

```json
{
    "extra_work_requests": [
        {
            "id": 51,
            "employee_name": "John Doe",
            "employee_code": "EMP-001",
            "username": "john.doe",
            "initials": "JD",
            "department": "Engineering",
            "work_date": "Oct 24, 2024",
            "time_range": "09:00 AM - 05:00 PM",
            "working_from": "Office",
            "work_icon": "work_history",
            "work_color": "text-primary",
            "approval_status": "PENDING",
            "status_bg": "bg-pending-bg",
            "status_text": "text-pending-text",
            "status_label": "Pending",
            "datetime": {
                "date": "Oct 24",
                "time": "09:15 AM",
                "full": "Oct 24, 09:15 AM"
            },
            "is_unread": true,
            "user_action": null,
            "user_action_status": null,
            "approver_name": null,
            "approver_level": null,
            "current_user_level": "SUPER_ADMIN"
        }
    ],
    "sidebar_employees": [
        {
            "id": 12,
            "name": "John Doe",
            "code": "EMP-001",
            "username": "john.doe",
            "initials": "JD"
        }
    ],
    "total_requests": 1,
    "pending_count": 1,
    "approved_count": 0,
    "rejected_count": 0,
    "new_count": 1,
    "has_clear_permission": true,
    "pagination": {
        "current_page": 1,
        "total_pages": 1,
        "total_records": 1,
        "page_size": 50,
        "has_next": false,
        "has_prev": false
    }
}
```

---

## Error Response

Status Code: `401 Unauthorized`

```json
{
    "detail": "Not authenticated"
}
```


================================================================================


# Clear Extra Work Inbox

## Overview
Deletes selected extra work requests from the inbox.
Requires the `extra_work.clear` permission (super admins have this by default).

---

## HTTP Method

`DELETE`

---

## API URL

```
{{BASE_URL}}/super_admin/extra_work/inbox/clear
```

---

## cURL Example

```bash
curl --location --request DELETE 'http://localhost:9000/super_admin/extra_work/inbox/clear' \
--header 'Cookie: access_token=<SESSION_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "request_ids": [51, 52, 53]
}'
```

---

## Request Body Parameters

| Field       | Type         | Required | Description                          |
|-------------|--------------|----------|--------------------------------------|
| request_ids | list[integer]| Yes      | List of extra work request IDs to delete |

---

## Request Body Example

```json
{
    "request_ids": [51, 52, 53]
}
```

---

## Success Response

Status Code: `200 OK`

```json
{
    "success": true,
    "message": "Successfully deleted 3 extra work request(s)",
    "deleted_count": 3
}
```

---

## Error Response

Status Code: `403 Forbidden`

```json
{
    "detail": "Missing permission: extra_work.clear"
}
```

Status Code: `200 OK` (empty request_ids)

```json
{
    "success": false,
    "message": "No request IDs provided",
    "deleted_count": 0
}
```


================================================================================


# Extra Work Approval Page

## Overview
Renders the Extra Work Approval detail HTML page for a specific request.
Accessible by super admins, users with `extra_work.view` permission, or designated approvers.

---

## HTTP Method

`GET`

---

## API URL

```
{{BASE_URL}}/super_admin/extra_work/approval/{work_id}
```

---

## cURL Example

```bash
curl --location 'http://localhost:9000/super_admin/extra_work/approval/51' \
--header 'Cookie: access_token=<SESSION_TOKEN>'
```

---

## Path Parameters

| Field   | Type    | Required | Description                   |
|---------|---------|----------|-------------------------------|
| work_id | integer | Yes      | ID of the extra work request  |

---

## Success Response

Status Code: `200 OK`

Returns HTML page (sh_extra_work_approval.html).
Page data is loaded separately via /approval/{work_id}/data endpoint.

---

## Error Response

Status Code: `403 Forbidden`

Returns unauthorized.html with message:
"You don't have permission to access Extra Work Approval."


================================================================================


# Extra Work Approval Data

## Overview
Fetches full detail of an extra work request including employee info, approval hierarchy,
leave balance, work history, and action permissions for the current user.

---

## HTTP Method

`GET`

---

## API URL

```
{{BASE_URL}}/super_admin/extra_work/approval/{work_id}/data
```

---

## cURL Example

```bash
curl --location 'http://localhost:9000/super_admin/extra_work/approval/51/data' \
--header 'Cookie: access_token=<SESSION_TOKEN>'
```

---

## Path Parameters

| Field   | Type    | Required | Description                   |
|---------|---------|----------|-------------------------------|
| work_id | integer | Yes      | ID of the extra work request  |

---

## Success Response

Status Code: `200 OK`

```json
{
    "work_id": 51,
    "can_approve": true,
    "can_reject": true,
    "approval_denial_reason": null,
    "level": "SUPER_ADMIN",
    "my_action_status": "pending",
    "employee": {
        "id": 12,
        "name": "John Doe",
        "code": "EMP-001",
        "username": "john.doe",
        "photo_url": "/api/employee/12/photo?v=abc12345",
        "department": "Engineering",
        "email": "john.doe@company.com",
        "timezone": "Asia/Dhaka"
    },
    "work": {
        "work_date": "Oct 24, 2024",
        "time_range": "09:00 AM - 05:00 PM",
        "working_from": "Office",
        "description": "Extra work on Oct 24, 2024 from Office",
        "joining_date": "N/A",
        "status": "PENDING",
        "status_label": "Pending Approval",
        "status_color": "#f59e0b",
        "request_sent": {
            "date": "Oct 24, 2024",
            "time": "09:15 AM",
            "full": "Oct 24, 2024, 09:15 AM"
        },
        "half_day_type": null
    },
    "approvers": [
        {
            "id": 5,
            "name": "Jane Smith",
            "initials": "JS",
            "level": 1,
            "designation": "HR Manager",
            "status": "pending",
            "remarks": null,
            "action_taken_at": null
        }
    ],
    "approver_info": null,
    "history": [
        {
            "date": "Oct 10, 2024",
            "working_from": "Home",
            "status": "APPROVED",
            "status_label": "Approved",
            "status_color": "#10b981"
        }
    ],
    "balance": {
        "year": 2024,
        "allowed": 20.0,
        "redeemed": 5.0,
        "available": 15.0,
        "achieved": 2.0,
        "carry_forward": 0.0
    },
    "all_remarks": [],
    "current_year": 2024
}
```

---

## Error Response

Status Code: `404 Not Found`

```json
{
    "detail": "Extra work request not found"
}
```

Status Code: `403 Forbidden`

```json
{
    "detail": "You don't have permission to access this Extra Work Request. You need 'extra_work.view' permission or be a designated approver."
}
```


================================================================================


# Extra Work Approval Action

## Overview
Performs approve, reject, or remark action on an extra work request.
Only Level 1 approvers and Super Admins update the main request status and leave balance.
Sends email notification to employee in the background when status changes.

---

## HTTP Method

`POST`

---

## API URL

```
{{BASE_URL}}/super_admin/extra_work/approval/{work_id}/action
```

---

## cURL Example

```bash
curl --location 'http://localhost:9000/super_admin/extra_work/approval/51/action' \
--header 'Cookie: access_token=<SESSION_TOKEN>' \
--form 'action="approve"' \
--form 'half_day_type="FULL_DAY"' \
--form 'remarks="Approved for weekend shift"' \
--form 'notify_employee="true"'
```

---

## Path Parameters

| Field   | Type    | Required | Description                   |
|---------|---------|----------|-------------------------------|
| work_id | integer | Yes      | ID of the extra work request  |

---

## Form Body Parameters

| Field           | Type   | Required                        | Description                                           |
|-----------------|--------|---------------------------------|-------------------------------------------------------|
| action          | string | Yes                             | Action to take: `approve`, `reject`, or `remark`     |
| half_day_type   | string | Yes (when action = approve)     | `FULL_DAY`, `FIRST_HALF`, or `SECOND_HALF`           |
| remarks         | string | No                              | Optional remarks/comments                             |
| notify_employee | string | No                              | Send email to employee: `"true"` or `"false"` (default: `"false"`) |

---

## Request Body Example (Approve)

```
action=approve
half_day_type=FULL_DAY
remarks=Approved for weekend shift
notify_employee=true
```

## Request Body Example (Reject)

```
action=reject
remarks=Insufficient justification
notify_employee=true
```

## Request Body Example (Remark only)

```
action=remark
remarks=Please provide more details
```

---

## Success Response

Status Code: `200 OK` (Level 1 / Super Admin)

```json
{
    "success": true,
    "message": "Extra work request has been approved",
    "is_level_1": true,
    "old_approval_status": "PENDING",
    "new_approval_status": "APPROVED",
    "email_sent": true,
    "status_changed": true,
    "was_already_finalized": false
}
```

Status Code: `200 OK` (Level 2+ approver - individual decision only)

```json
{
    "success": true,
    "message": "Your decision has been recorded (Level 2)",
    "is_level_1": false
}
```

Status Code: `200 OK` (Remark action)

```json
{
    "success": true,
    "message": "Remark posted successfully",
    "work_id": 51,
    "action": "remark"
}
```

---

## Error Response

Status Code: `400 Bad Request`

```json
{
    "detail": "half_day_type is required when approving. Select Full Day, First Half, or Second Half."
}
```

Status Code: `400 Bad Request` (invalid action)

```json
{
    "detail": "Invalid action. Must be 'approve', 'reject', or 'remark'"
}
```

Status Code: `403 Forbidden`

```json
{
    "detail": "You have already approved this request and cannot change your decision"
}
```

Status Code: `404 Not Found`

```json
{
    "detail": "Extra work request not found"
}
```
