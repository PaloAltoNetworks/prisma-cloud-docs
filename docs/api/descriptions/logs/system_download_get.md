This endpoint will return the system debug logs with `tar.gz` file extension.


The following example curl command uses basic auth to download the logs:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o {file_name}.tar.gz
  https://<CONSOLE>:8083/api/v1/logs/system/download
```
