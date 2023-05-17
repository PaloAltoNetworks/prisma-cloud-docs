Configures the timeout for Prisma Cloud Compute sessions.

For more information, see [Logon Settings](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/configure/logon_settings).

## cURL Request

Refer to the following example cURL request that uses basic auth to set the timeout to 900 seconds (15 minutes):

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '{"sessionTimeoutSec": 900}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/logon"
```
