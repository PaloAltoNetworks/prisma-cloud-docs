Configures the custom certificate for securing browser access to the Console. 

These settings can be seen in the console under **Manage > Authentication > System Certificates**.

For the custom TLS certificate for securing browser access, this file must be in the concatenated public cert and private key in PEM format. For more information about this configuration, see [Custom certs for Console access](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/configure/custom_certs_predefined_dir)

## cURL Request

Refer to the following example cURL request that uses basic auth and configures the custom certificate to use for securing browser access to the console:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"consoleCustomCert":"....."}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/console-certificate"
```
