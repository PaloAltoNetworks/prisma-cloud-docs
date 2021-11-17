Re-scan all containers immediately.
This endpoint returns the time that the scans were initiated.

The following example command uses curl and basic auth to force Prisma Cloud Compute to re-scan all containers:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/containers/scan
```
