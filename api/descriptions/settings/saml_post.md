Configures the SAML settings that is used to authenticate to the Prisma Cloud Compute.

For more information, see [Okta via SAML 2.0](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/saml), [G Suite via SAML](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/saml_google_g_suite), [Azure AD via SAML](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/saml_azure_active_directory), [PingFederate via SAML](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/saml_ping_federate), and [ADFS via SAML](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/saml_active_directory_federation_services).

## cURL Request

Refer to the following example cURL request that uses the basic auth to set up and enable the SAML integration with Prisma Cloud Compute:

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
  "https://<CONSOLE>/api/v<VERSION>/settings/saml"
```
