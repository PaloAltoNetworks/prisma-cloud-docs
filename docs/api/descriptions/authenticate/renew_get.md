Renews an old (unexpired) access token and returns a new token.

### cURL Request

The following cURL command retrieves a new access token using an old access token.

```bash
$ curl -k \
  -H "Authorization: Bearer <OLD_ACCESS_TOKEN>" \
   https://<CONSOLE>/api/v1/authenticate/renew
```

### Response

A successful response will return the following response containing the new access token.
This access token replaces the old access token.

```bash
{"token", "ACCESS_TOKEN_VALUE"}
```