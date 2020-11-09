Downloads all container scan reports in CSV format.

A call to this api endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/containers/download
  > container_report.csv
```
