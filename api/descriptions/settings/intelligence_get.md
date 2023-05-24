Returns the details about the Intelligence Stream configuration.

### cURL Request

Refer to the following example cURL command that uses basic auth to retrieve your Intelligence Stream configuration settings.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/intelligence"
```
