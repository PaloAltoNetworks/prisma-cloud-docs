Retrieves the version number for Console.

### cURL Request

The following cURL command retrieves the version number for Console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/version
```

A successful response returns the version number for Console.
