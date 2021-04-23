Retrieves all deployed Defenders.

This endpoint maps to the table in **Manage > Defenders > Defenders** in the Console UI.

### cURL Request

The following command cURL command retrieves all deployed Defenders.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/defenders
```

A successful response returns all deployed Defenders.
