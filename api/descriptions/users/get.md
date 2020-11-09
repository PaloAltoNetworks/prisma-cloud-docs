Retrieves a list of all users.

The following example curl command uses basic auth to retrieve all users.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/users
```
