Retrieves a list of all credentials from the credentials store.
This endpoint maps to **Manage > Authentication > Credentials store** in the Console UI.

### cURL Request

Refer to the following example cURL command that retrieves all credentials:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/credentials
```

A successful response returns a list of all credentials.
