Creates the initial admin user after Console is first installed.

Although this endpoint is supported, no backwards compatibility is offered for it.

### cURL Request

The following cURL command creates the initial admin user with the username `admin` and password `password`.

```bash
$ curl -k \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"username": "admin", "password": "password"}' \
  https://<CONSOLE>/api/v1/signup
```

**Note:** The username and password values are case-sensitive.

### Responses

**Success Response:** No response will return if the user creation is successful.

```bash
{"token", "ACCESS_TOKEN_VALUE"}
```

**Error Response:** An error response will return the following response if the initial sign up process was previously completed.

```bash
{"err":"system already initialized"}
```
