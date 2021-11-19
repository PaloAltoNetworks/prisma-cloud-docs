Retrieves the details and state of each host service runtime model in CSV format.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o {local_file_name} \
  https://<CONSOLE>:8083/api/v1/profiles/host/download
```
