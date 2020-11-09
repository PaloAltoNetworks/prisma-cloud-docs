Retrieves a list of image names from current scanned registry images. The base `/api/v1/registry` endpoint takes repositories listed in this response as the `names` query.

The following example curl command uses basic auth to retrieve a list of image names from your scanned registry images:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/registry/names
```
