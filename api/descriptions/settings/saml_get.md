Returns the configured SAML settings that is used to authenticate to the Prisma Cloud Compute console.

## cURL Request

Refer to the following example cURL request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/settings/saml
```
