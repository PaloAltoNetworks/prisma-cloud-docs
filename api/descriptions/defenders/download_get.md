Downloads information about deployed Defenders in CSV format.
Use the query parameters to filter what data is returned.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/download
```
