Retrieves an access token using a client certificate.
This endpoint checks the supplied client certificate and authorizes the user based on the username in the certificate's CN or UPN field.
By default, access tokens are valid for 24 hours.

The following example curl command retrieves a token using a client certificate:

```bash
$ curl -k \
  -X POST \
  --cert <CERT.PEM>
  https://<CONSOLE>:8083/api/v1/authenticate-client
```

Where the certificate must be in PEM format, and the certificate file must consist of a private key and client certificate concatenated together.
