Checks if Console is reachable over the network from the host where you call the endpoint.
If you get a response code of 200, the request succeeded, and Console is both alive and reachable.

The following curl command pings Console and prints the HTTP response code.

```bash
$ curl -k \
  -s \
  -o /dev/null \
  -w "%{http_code}\n" \
  -X GET \
  https://<CONSOLE>:8083/api/v1/_ping
```
