Returns the current learned connections from CNNF (for hosts) in JSON format.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o <export.json> \
  https://<CONSOLE>:8083/api/v1/radar/host/export
```
