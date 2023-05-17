Enables authentication for just an explicit list of trusted certificates.

Use this endpoint to control how users authenticate to Prisma Cloud Compute.
Users employ client certificates to authenticate commands sent from a Docker client through Prisma Cloud Compute.

> **_NOTE:_** This feature can only be enabled if a custom certificate authority has been configured.
For more information, see the `/settings/certificates` endpoint.

## cURL Request

Refer to the following example cURL request that uses basic auth to enable this feature:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '{"enabled" : true }'
  "https://<CONSOLE>/api/v<VERSION>/settings/trusted-certificates"
```
