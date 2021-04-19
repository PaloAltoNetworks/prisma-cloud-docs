Retrieves a list of all credentials from the credentials store.
This endpoint maps to the credentials table in **Manage > Authentication > Credentials store** in the Console UI.

### cURL Request

The following cURL command retrieves all credentials:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/credentials
```

A successful response returns a list of all credentials.
