Retrieves a list of tags.

### cURL Request

Refer to the following example cURL command that retrieves a list of tags:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/tags"
```
A successful response returns a list of defined tags.