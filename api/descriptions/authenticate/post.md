Retrieves an access token using your username and password.
By default, access tokens are valid for 24 hours.

### cURL Request

The following cURL command retrieves a token for user `admin` with password `password`.

```bash
$ curl -k \
  -H "Content-Type: application/json" \
  -X POST \
  -d \
'{
   "username":"admin",
   "password":"password"
}' \
  https://<CONSOLE>/api/v1/authenticate
```

**Note:** The username and password values are case-sensitive.

### Response

A successful response will return the following response containing the access token which can be used for the rest of the API endpoints.

```bash
{"token", "ACCESS_TOKEN_VALUE"}
```
