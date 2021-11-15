Retrieves all scan reports for the serverless functions which Prisma Cloud has been configured to scan.

This endpoint maps to the table in **Monitor > Vulnerabilities > Functions > Scanned functions** in the Console UI.

### cURL Request

The following cURL command retrieves the scan reports for serverless functions:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/serverless
```

A successful response returns the scan reports.
