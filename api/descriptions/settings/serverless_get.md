This endpoint will return any configured serverless function scanners found in **Defend > Vulnerabilities > Functions**.

The following example curl command uses basic auth to retrieve serverless settings in an array, sorted by Cloud Provider:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/serverless
```
