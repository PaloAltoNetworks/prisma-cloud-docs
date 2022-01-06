This endpoint will return the configured SAML settings configured to authenticate to the Prisma Cloud Compute console.

The following example curl command uses basic auth to retrieve you SAML settings:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/saml
```
