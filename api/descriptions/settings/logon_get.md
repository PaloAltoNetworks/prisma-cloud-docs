Configures various logon settings.

The following example curl command uses basic auth to retrieve all current logon settings.

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/logon"
```
