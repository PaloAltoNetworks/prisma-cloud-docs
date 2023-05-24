Configures the logon settings.

## cURL Request

Refer to the following example cURL request that uses basic auth to retrieve all current logon settings.

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/logon"
```
