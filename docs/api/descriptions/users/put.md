Updates an existing user in the system.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Users**.
2. In a table row, click the **Actions** button for the user to update.
3. Click the **Manage** button and update the user's parameters.
4. Click the **Save** button to save the updated user.

### cURL Request

The following example command changes the role of a user to `auditor`.

In general, you should get the user object from `GET /api/v<VERSION>/users` and resubmit all key-value pairs, changing just the values that need updating.
If key-values are left unspecified, their default values will override any current values (note the exception below).
For example, if `permissions.collections` specified a collection named `finance-app`, but the submitted request omitted `permissions.collections`, its value would be reset to `All`.

For "local" users, where `authType` is set to `basic`: if a password isn't specified, it's left as-is.
For any other `authType`, passwords are managed by the identity provider (IdP), and aren't specified in the request body.

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/users' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "username":"<ID>",
   "role":"auditor",
   "authType":"basic",
   "permissions":[
      {
         "project":"<PROJECT_NAME>",
         "collections":[
            "All"
         ]
      }
   ]   
}'
```

**Note:** No response will be returned upon successful execution.
