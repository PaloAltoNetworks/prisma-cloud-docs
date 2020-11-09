Stops current VM image scan immediately.

The following example command uses curl and basic auth to force Prisma Cloud to stop scanning all VM images:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/vms/stop
```
