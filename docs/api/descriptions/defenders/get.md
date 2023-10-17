Retrieves all deployed Defenders.

This endpoint maps to the UI Console page in **Manage > Defenders > Defenders**.

### cURL Request

Refer to the following example cURL command that retrieves all deployed Defenders.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/defenders
```

A successful response returns all deployed Defenders.
