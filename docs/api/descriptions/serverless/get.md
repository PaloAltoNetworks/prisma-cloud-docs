Retrieves all scan reports for the serverless functions which Prisma Cloud has been configured to scan.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds.
You get an HTTP error response 429 if the limit exceeds.

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
