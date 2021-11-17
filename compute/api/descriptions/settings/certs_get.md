Gets the Subject Alternative Name(s) (SANs) in Console's certificate.
Defenders use these names to connect to Console.

The following example curl command uses basic auth to retrieve the SANs in Console's cert:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/certs
```
