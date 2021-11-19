Manage details associated with client certificates.
Users employ client certificates to authenticate commands sent from the Docker client through Prisma Cloud Compute.

This endpoint lets you specify a certificate authority (CA) to trust, and the validity period for client certs.

The following example curl command uses basic auth to set the validity period for client certificates to seven days.

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '{"certificatePeriodDays": 7} ' \
  https://<CONSOLE>:8083/api/v1/settings/certificates
```
