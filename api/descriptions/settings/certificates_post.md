Sets a certificate authority (CA) to trust and the validity period for client certificates.

Use client certificates to authenticate commands sent from the Docker client through Prisma Cloud Compute.

For more information, see [Certificates](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/configure/certificates).

## cURL Request

Refer to the following example cURL request that uses basic auth to set the validity period for client certificates to seven days:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '{"certificatePeriodDays": 7} ' \
  "https://<CONSOLE>/api/v<VERSION>/settings/certificates"
```
