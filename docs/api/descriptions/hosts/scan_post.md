Re-scan all hosts immediately.

Refer to the following example command that forces Prisma Cloud Compute to re-scan all hosts:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>/api/v<VERSION>/hosts/scan
```
