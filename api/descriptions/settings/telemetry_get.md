Returns the telemetry settings that anonymously reports the threats and vulnerabilities to Prisma Cloud Compute.

For more information, see [telemetry](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/technology_overviews/telemetry) article.

## cURL Request

Refer to the following example cURL request that retrieves the settings if telemetry is enabled or not:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/telemetry"
```
