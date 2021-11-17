Returns the connection status of the intelligence stream and the last intelligence stream update.

The following is an example curl using basic auth to find the intelligence stream status:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/statuses/intelligence
```
