This endpoint will return the defender logs with `tar.gz` file extension given the hostname of the defender.

The hostname can be returned from the endpoint `/defenders/names`

The following example curl command uses basic auth to download the logs:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o defender_logs.tar.gz
  https://<CONSOLE>:8083/api/v1/logs/defender/download?hostname={hostname}
```
