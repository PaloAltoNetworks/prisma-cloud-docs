Retrieves the details and state of all host service runtime models in CSV format

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o profiles-service.csv \
  https://<CONSOLE>:8083/api/v1/profiles/service/download
```
