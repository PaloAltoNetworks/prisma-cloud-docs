Stops current registry scan immediately.

The following example command uses curl and basic auth to force Prisma Cloud Compute to stop scanning all registry images:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/registry/stop
```
