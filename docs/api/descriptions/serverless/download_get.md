Downloads all serverless scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Functions > Scanned functions** in the Console UI.

### cURL Request

The following cURL command retrieves a list of all serverless resources monitored by Prisma Cloud Compute and saves the results in a CSV file called `serverless.csv`:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/serverless/download' \
  > serverless.csv
```

A successful response displays the status of the download.
