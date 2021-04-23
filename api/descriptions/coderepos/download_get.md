Downloads code repository scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Code repositories** in the Console UI.

### cURL Request

The following cURL command generates a CSV file containing the reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/coderepos/download" \
  > coderepos.csv
```

A successful response displays the status of the download.
