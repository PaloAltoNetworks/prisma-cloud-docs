Changes the password of a user.

To invoke this endpoint in the Console UI:

1. Click on the user icon near the top-right corner of the Console UI.
2. Select **Change password**.
3. Enter the old and new passwords.
3. Click the **Save** button.

### cURL Request

The following cURL command replaces the password of `USER` (the user authenticating with Console to call this endpoint).

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/users/password' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
    "oldPassword": "<OLD_PASSWORD>", 
    "newPassword": "<NEW_PASSWORD>"
}'
```

**Note:** No response will be returned upon successful execution.
