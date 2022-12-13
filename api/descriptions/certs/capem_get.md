Retrieves the Base64-encoded SSL root certificate self-signed by primary certificate authority (CA) in PEM format.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/certs/ca.pem"
```

### cURL Response

```
-----BEGIN CERTIFICATE-----
MIIDHDCCAgSgAwIBAgIQDBOoX575awe…iQ6j6Icf8NDANBgkqhkiG9w0BAQsFADAo
MRIwEAYDVQQKEwlUd2lzdGxvY2sxEjAQBgNVBAMTCVR3aXN0bG9jazAeFw0yMjEx
MDgxNjA1MDBaFw0yNTExMDrbXDQLhFyPXcFfNgNdEaH
EbVjIec/Frhk0TWIhDDphuwaIz2Qkuj/hIF1rtHhkMFXsYKsUGDcyGKJnEUxz9zR
S4hdrn5QhEh+m+CLzuv+WRV925WJ5rCKYeT9DIhXgEM=
-----END CERTIFICATE-----
```