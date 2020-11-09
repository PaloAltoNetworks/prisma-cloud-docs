Re-scans all VM images immediately. This endpoint returns the time that the scans were initiated.

The following example command uses curl and basic auth to force Prisma Cloud to re-scan all VM images:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/vms/scan
```
