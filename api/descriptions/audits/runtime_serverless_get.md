Returns scan reports in JSON format for any serverless functions you've configured Prisma Cloud Compute to scan.

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://CONSOLE_ADDRESS:PORT/api/v1/audits/runtime/serverless 
```
