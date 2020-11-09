Retrieve a list of all alert profiles created in the system.

The following example curl command uses basic auth to retrieve all alert profiles:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/alert-profiles
```
