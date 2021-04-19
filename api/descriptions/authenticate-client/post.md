Retrieves an access token using a client certificate.
This endpoint checks the supplied client certificate and authorizes the user based on the username in the certificate's CN or UPN field.

### cURL Request
The following example curl command retrieves a token using a client certificate.

**Note:** the certificate must be in PEM format, and the certificate file must consist of a client certificate concatenated together with a private key.

```bash
$ curl -k \
  -X POST \
  --cert <CERT.PEM>
  https://<CONSOLE>/api/v1/authenticate-client
```

A successful response returns the user's role and an access token.
Use the token for subsequent calls to the API.

```bash
{
    "admin",
    "<ACCESS_TOKEN>"
}
```
