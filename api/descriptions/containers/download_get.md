Downloads all container scan reports in CSV format.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/containers/download
  > container_report.csv
```
