Retrieves a list of all host audits that match the query.

The following example curl command uses basic auth to retrieve all host audits:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/runtime/host
```
