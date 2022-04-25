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

Refer to the following example cURL command that retrieves a list of connected Defenders using a query parameter and a specified boolean value in lower case:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/defenders/names?connected=true"
```

Refer to the following example cURL command that retrieves a list of disconnected Defenders using a query parameter and a specified boolean value in lower case:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/defenders/names?connected=false"
```
**Note**: The query parameter `connected` expects and accepts a boolean value in lower case. 
The endpoint enlists all the connected and disconnected Defenders if do not specify a boolean value.

Refer to the following example cURL command that retrieves a list of Defenders by type:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/defenders/names?type=<linux|windows|docker|...>"
```
