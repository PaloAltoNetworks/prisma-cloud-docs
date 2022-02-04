Creates a group with users.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Groups**.
2. Add a collection using **+ Add group**.
3. Enter a group name and add at least one user.
3. Click the **Save** button.

### cURL Request

Refer to the following example cURL command that creates a new group named `my-group`:

```bash
$ curl -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "groupName": "my-group",
   "user": [
   		{"username": "john"},
   		{"username": "jane"}
   	]
}' \
'https://<CONSOLE>/api/v<VERSION>/groups'
```
This group includes the users associated with the usernames `john` and `jane`.

**Note:** You must use usernames that already exist in the system.

No response will be returned upon successful execution.
