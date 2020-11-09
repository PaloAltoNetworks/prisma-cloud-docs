Retrieves an access token using your username and password.
By default, access tokens are valid for 24 hours.

The following example curl command retrieves a token for user 'admin' with password 'admin':

```bash
$ curl -k \
  -H "Content-Type: application/json" \
  -X POST \
  -d \
'{
   "username":"admin",
   "password":"admin"
}' \
  https://<CONSOLE>:8083/api/v1/authenticate
```
