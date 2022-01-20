Downloads information about deployed Defenders in CSV format.
Use the query parameters to filter what data is returned.

**Note:** The results contain "hostname" even if you don't specify a "hostname" in the "fields" query parameter.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/download
```
