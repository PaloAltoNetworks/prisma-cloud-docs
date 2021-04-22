Downloads all VM image scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Hosts > VM images** in the Console UI.

### cURL Request

The following cURL command retrieves all VM image scan reports and saves the results in a CSV file called `vm_images_scan.csv`:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/vms/download \
  > vm_images_scan.csv
```

A successful response displays the status of the download.
