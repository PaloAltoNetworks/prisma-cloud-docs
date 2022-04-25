Retrieves all scan reports for the serverless functions which Prisma Cloud has been configured to scan.

This endpoint maps to **Monitor > Vulnerabilities > Functions > Scanned functions** in the Console UI.

### cURL Request

Refer to the following example cURL command that retrieves the scan reports for serverless functions:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/serverless
```

A successful response returns the scan reports.
