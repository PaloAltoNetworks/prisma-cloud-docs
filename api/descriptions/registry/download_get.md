Downloads registry image scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Compliance > Images > Registries** in the Console UI.

### cURL Request

Refer to the following cURL command that generates a CSV file containing the scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry/download" \
  > registry_report.csv
```

A successful response displays the status of the download.
