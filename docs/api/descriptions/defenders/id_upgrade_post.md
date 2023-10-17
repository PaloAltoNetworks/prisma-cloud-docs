Upgrades Defender on `<HOSTNAME>`.

`<HOSTNAME>` is a single list item from the `/api/v<VERSION>/defenders/names` endpoint.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>/api/v<VERSION>/defenders/<HOSTNAME>/upgrade
```
