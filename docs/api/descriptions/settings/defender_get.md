Returns the advanced settings for Defenders.

### cURL Request

Refer to the following example cURL command that gets all advanced settings for Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/settings/defender'
```

A successful response returns all advanced settings for Defenders.
