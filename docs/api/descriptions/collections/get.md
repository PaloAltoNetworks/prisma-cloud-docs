Retrieves a list of all collections.

This endpoint maps to the table in **Manage > Collections and Tags > Collections** in the Console UI.

### cURL Request

Refer to the following example cURL command that returns a list of collections:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/collections'
```
