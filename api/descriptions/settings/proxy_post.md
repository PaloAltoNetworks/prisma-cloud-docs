Configures the proxy settings.

For more information, see [Proxy Settings](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/configure/proxy).

## cURL Request

Refer to the following example cURL request that specifies the proxy to use to access the Internet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "httpProxy":"http://proxyserver.example.com:8282"
}' \
  https://<CONSOLE>/api/v<VERSION>/settings/proxy
```
