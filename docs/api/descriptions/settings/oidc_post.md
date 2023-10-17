Configures the OpenID Connect settings.

For more information, see [OIDC](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/oidc).

## cURL Request

Refer to the following example cURL request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -d '{"enabled": true,"clientID":"0oajdm6atavfYyJfr4x6","clientSecret":{"encrypted":"rnEk+1be20FLv+BYnDX4s5/T0NOb49hkNkaZQtgiF7K2s65"},"groupScope":"groups","groupClaim":"groups","openIDIssuesURL":"https://ss-123456.okta.com","providerAlias":"oidc_okta_ss"}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/oidc"
```