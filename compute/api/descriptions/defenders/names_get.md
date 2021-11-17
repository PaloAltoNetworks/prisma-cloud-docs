Retrieves a list of Defender hostnames that can be used as the `{id}` query parameter in other `/api/v1/defenders` endpoints.

Retrieve a list of all Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/names
```

Retrieve a list of connected Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/names?connected
```

Retrieve a list of Defenders by type:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/names?type=<linux|windows|docker|...>
```
