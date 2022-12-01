Downloads all VM image scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Hosts > VM images** in the Console UI.

### cURL Request

Refer to the following example cURL command that retrieves all VM image scan reports and saves the results in a CSV file called `vm_images_scan.csv`:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o vm_images_scan.csv \
  "https://<CONSOLE>/api/v<VERSION>/vms/download"
```

A successful response displays the status of the download.
