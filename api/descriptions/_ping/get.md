Checks if Console is reachable from your network host.

### cURL Request

The following cURL command pings Console and prints the HTTP response code:

```bash
$ curl -k \
  -s \
  -o /dev/null \
  -w "%{http_code}\n" \
  -X GET \
  https://<CONSOLE>/api/v1/_ping
```