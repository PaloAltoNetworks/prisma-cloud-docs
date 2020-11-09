Downloads a list of all management audits into CSV format.

The following example curl command uses basic auth to retrieve all management audits

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/mgmt/download -o aqsa.csv
```
