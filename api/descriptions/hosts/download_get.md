Downloads all host scan reports in CSV format.

A curl command to access this endpoint may resemble the following code snippet:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/hosts/download \
  > hosts_scan.csv
```
