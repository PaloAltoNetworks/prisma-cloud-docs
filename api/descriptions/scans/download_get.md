Downloads all scan reports from the Jenkins plugin and twistcli in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Images > CI** in the Console UI.

### cURL Request

The following cURL command retrieves and saves your Jenkins and twistcli scan reports to a CSV file called `scans_report.csv`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/scans/download \
  > scans_report.csv
```

A successful response displays the status of the download.
