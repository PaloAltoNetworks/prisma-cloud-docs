Downloads container scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Compliance > Images > Deployed** in the Console UI.

**Note**: The query parameter `fields` is not supported for this API endpoint.

### cURL Request

Refer to the following example cURL command that generates a CSV file containing the scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/containers/download?id={id}&layers=true" \
  > container_report.csv
```

A successful response displays the status of the download.
