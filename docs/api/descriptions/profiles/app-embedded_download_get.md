Downloads the app-embedded observations in a CSV format.

## cURL Request

Refer to the following example cURL command that downloads all the app-embedded runtime profiles:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o <FILE NAME> \
  'https://<CONSOLE>/api/v<VERSION>/profiles/app-embedded/download'
```