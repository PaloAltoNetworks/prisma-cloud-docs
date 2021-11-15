Returns the connection status for the Intelligence Stream, along with the time of the last update.

The following is an example curl using basic auth to find the intelligence stream status:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/statuses/intelligence
```
