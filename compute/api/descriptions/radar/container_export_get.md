Returns the current learned connections from CNNF (for containers) in JSON format.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o cnnf_containers_export.json \
  https://<CONSOLE>:8083/api/v1/radar/container/export
```
