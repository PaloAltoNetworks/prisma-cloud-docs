Retrieves a list of image names from current scanned registry images. The base `/api/v1/registry` endpoint takes repositories listed in this response as the `names` query.

## cURL Request

Refer to the following example cURL command that retrieves a list of image names from your scanned registry images:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/registry/names
```
