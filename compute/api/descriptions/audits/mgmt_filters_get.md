Retrieves a list of management audit types found in your environment. 
These fields can be further used as your queries to get management audit data.

The following example curl command retrieves all management audit filters

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/mgmt/filters
```
