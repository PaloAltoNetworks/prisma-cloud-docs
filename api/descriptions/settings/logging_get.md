Gets the logging settings.

The following example curl command uses basic auth to retrieve your logging details.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/settings/logging
```
