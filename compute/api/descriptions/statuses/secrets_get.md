Returns the connection status of any secret stores you have configured, as well as the last update to the secret store.

The following is an example curl using basic auth to find the secret store status:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/statuses/secrets
```
