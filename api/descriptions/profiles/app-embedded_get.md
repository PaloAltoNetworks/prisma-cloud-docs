Retrieves the app-embedded observations.

## cURL Request

Refer to the following example cURL command that lists all the app-embedded runtime:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/profiles/app-embedded'
```