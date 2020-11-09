Downloads all image scan reports in CSV format. You can redirect the output of the request to a csv file.

The following example curl command uses basic auth to retrieve and save your console's registry scan report to a csv file called `registry_report.csv`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/registry/download > registry_report.csv
```
