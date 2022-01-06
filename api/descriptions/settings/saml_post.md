This endpoint let's you configure SAML settings configured to authenticate to the Prisma Cloud Compute console.

The following example curl command uses basic auth to set up enable SAML integration with Prisma Cloud Compute, set the Identity provider to ADFS, set the Identity provide single sign-on URL to `https://my-adfs-server.twistlock.com/adfs/SSO`, set the Identity provider issuer to `https://my-adfs-server.twistlock.com/adfs/services/trust`, set the X.509 Certificate to `CERTIFICATE`, and to set the audience to `twistlock`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "enabled": true,
    "url": "https://my-adfs-server.twistlock.com/adfs/SSO",
    "cert": "<CERTIFICATE>",
    "issuer": "https://my-adfs-server.twistlock.com/adfs/services/trust",
    "type": "adfs",
    "audience": "twistlock",
    "appId": "",
    "tenantId": "",
    "appSecret": {
        "encrypted": ""
    }
    }' \
  https://<CONSOLE>:8083/api/v1/settings/saml
```
