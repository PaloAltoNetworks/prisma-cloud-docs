Downloads all host scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Hosts > Running hosts** in the Console UI.

**Note**: The query parameters `fields`, `complianceID` and `normalizedSeverity` are not supported for this API endpoint.

### cURL Request

Refer to the following example cURL command that downloads all host scan reports to a CSV file called `hosts_report.csv`:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET -o hosts_report.csv \
  https://<CONSOLE>/api/v<VERSION>/hosts/download
```

A successful response displays the status of the download.
