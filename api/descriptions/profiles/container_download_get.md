Retrieves the details and state of all runtime models in CSV format

The following example command uses curl to download a complete list in CSV format.

NOTE: the -o option can help with saving the data to a file

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o {local_file_name} \
  https://<CONSOLE>:8083/api/v1/profiles/container/download
```
