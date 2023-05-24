Returns the logging settings.

## cURL Request

Refer to the following example cURL request that uses basic auth to retrieve your logging details.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/logging"
```
