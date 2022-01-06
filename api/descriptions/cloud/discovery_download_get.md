Downloads all cloud scan data in a CSV file.

### cURL Request

Refer to the following cURL example command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o cloud-discovery.csv \
  https://<CONSOLE>:8083/api/v<VERSION>/cloud/discovery/download
```
