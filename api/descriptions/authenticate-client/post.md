Retrieves an access token using a client certificate.
This endpoint checks the supplied client certificate and authorizes the user based on the username in the certificate's CN or UPN field.

**Note:** The certificate must be in PEM format, and the certificate file must consist of a client certificate concatenated together with a private key.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -X POST \
  --cert <CERT.PEM> \
  https://<CONSOLE>/api/v<VERSION>/authenticate-client
```

### Response

Refer to the following example cURL response that returns the user's role and an access token that you can use for subsequent API calls: 

```bash
{
    "admin",
    "<ACCESS_TOKEN>"
}
```
