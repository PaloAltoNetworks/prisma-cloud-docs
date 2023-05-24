Configures the OAuth settings.

For more information, see [GitHub OAuth](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/oauth2_github) and [OpenShift](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/oauth2_openshift)

## cURL Request

Refer to the following example cURL response:

```bash
curl -k \        
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"clientID":"ef3a806a249a31b7d15e","clientSecret":{"encrypted":"O27GsQ7PDX4LrVx6q+A7sMLUAKTbKU3DAYTZyaOhqTqdNwI7raKFCA3/RrmRPUgk"},"providerName":"github","authURL":"https://github.com/login/oauth/authorize","tokenURL":"https://github.com/login/oauth/access_token","providerAlias":"github_ss"}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/oauth"
```
