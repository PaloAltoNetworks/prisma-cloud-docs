Gets the advanced settings for Defenders.

### cURL Request

The following cURL command gets all advanced settings for defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/settings/defender'
```

A successful response returns all advanced settings for defenders.
