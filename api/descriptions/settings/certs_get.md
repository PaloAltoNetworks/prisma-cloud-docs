Returns the Subject Alternative Name(s) (SANs) in Console's certificate.
Defenders use these names to connect to Console.

## cURL Request

Refer to the following example cURL request that uses basic auth to retrieve the SANs in Console's cert:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/certs"
```
