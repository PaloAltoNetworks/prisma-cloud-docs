Restarts Defender on a given host.

`<HOSTNAME>` is a single list item from the `/api/v1/defenders/names` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/defenders/<HOSTNAME>/restart
```
