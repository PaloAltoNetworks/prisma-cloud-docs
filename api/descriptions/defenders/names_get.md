Retrieves a list of Defender hostnames that can be used as the `{id}` query parameter in other `/api/v1/defenders` endpoints.

### cURL Request

Refer to the following example cURL command that retrieves a list of all Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/defenders/names
```

Refer to the following example cURL command that retrieves a list of connected Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/defenders/names?connected"
```

Refer to the following example cURL command that retrieves a list of Defenders by type:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/defenders/names?type=<linux|windows|docker|...>"
```
