Downloads information about deployed Defenders in CSV format.
Use the query parameters to filter what data is returned.

**Note:** The results contain "hostname" even if you don't specify a "hostname" in the "fields" query parameter.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET -o <FILENAME> \
  https://<CONSOLE>/api/v<VERSION>/defenders/download
```
