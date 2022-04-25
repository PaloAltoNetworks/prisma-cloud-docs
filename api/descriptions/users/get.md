Retrieves a list of all users.

This endpoint maps to **Manage > Authentication > Users** in the Console UI.

### cURL Request

The following cURL command retrieves all users.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/users'
```

A successful response returns a list of all users.
