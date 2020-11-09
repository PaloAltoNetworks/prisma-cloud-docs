Retrieves a list of all trusted images.

The following example curl command uses basic auth to retrieve all trusted images:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/trust
```
