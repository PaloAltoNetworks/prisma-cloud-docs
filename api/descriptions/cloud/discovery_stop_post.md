Terminates a cloud discovery scan that's in progress.

### cURL Request

Refer to the following cURL example request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/cloud/discovery/stop
```
