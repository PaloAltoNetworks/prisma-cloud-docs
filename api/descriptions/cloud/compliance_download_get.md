Download all cloud scan data in CSV format.


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o cloud-compliance.csv \
  https://<CONSOLE>:8083/api/v1/cloud/compliance/download
```
