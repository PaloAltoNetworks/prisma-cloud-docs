Enables or disables the telemetry feature. 

For more information, see [telemetry](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/technology_overviews/telemetry) article.

## cURL Request

Refer to the following example cURL request that uses basic auth to turn off telemetry:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"enabled":false}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/telemetry"
```
