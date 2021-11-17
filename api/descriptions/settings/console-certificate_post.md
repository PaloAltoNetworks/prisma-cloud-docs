This endpoint will enter custom certificates for securing browser access to the Console. These settings can be seen in the console under **Manage > Authentication > System Certificates**.

For the custom TLS certificate for securing browser access, this file must be in the concatenated public cert and private key in PEM format. For more information about this configuration, see [Custom certs for Console access](https://docs.twistlock.com/docs/latest/configure/custom_certs_console_access.html)

The following example curl command uses basic auth enter the custom certificate to use for securing browser access to the console:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"consoleCustomCert":"....."}' \
  https://<CONSOLE>:8083/api/v1/settings/console-certificate
```
