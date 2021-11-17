Re-scan all serverless functions immediately.

The following example command uses curl and basic auth to force Prisma Cloud Compute to re-scan all serverless functions.

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/serverless/scan
```
