Returns the scan audit events data in CSV format for any configured serverless functions in Prisma Cloud Compute.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <runtime_serverless_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/serverless/download" 
```
