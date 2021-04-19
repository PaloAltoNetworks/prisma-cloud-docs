Downloads all host scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Hosts > Running hosts** in the Console UI.

### cURL Request

The following cURL command downloads all host scan reports to a CSV file called `hosts_report.csv`:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/hosts/download \
  > hosts_scan.csv
```

A successful response displays the status of the download.
