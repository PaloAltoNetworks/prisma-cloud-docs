Deletes a user from the system.

The URL parameter `{id}` maps to `username`.
The `username` for each user can be retrieved from the `GET /api/v<VERSION>/users` endpoint.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Users**.
2. In a table row, click the **Actions** button for the user to update.
3. Click the **Delete** button to open the delete confirmation window.
4. Click the **Delete User** button to delete the user.

**Note:** You can not delete the user for the current logged in account.

### cURL Request

The following cURL command deletes user `ID` from the system.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>/api/v<VERSION>/users/<ID>
```

**Note:** No response will be returned upon successful execution.
