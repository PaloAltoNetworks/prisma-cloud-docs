Retrieves an access token using your username and password.
By default, access tokens are valid for 30 minutes.
You can set the validity period in Console under **Manage > Authentication > Logon**.

**Note:** The username and password values are case-sensitive.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -H "Content-Type: application/json" \
  -X POST \
  -d \
'{
   "username":"admin",
   "password":"password"
}' \
  https://<CONSOLE>/api/v<VERSION>/authenticate
```

### Response

Refer to the following successful example response that returns the access token for use in other API endpoints:

```bash
{"token", "ACCESS_TOKEN_VALUE"}
```
