Stops current VM image scan immediately.

### cURL Request

Refer to the following example cURL command that forces Prisma Cloud to stop scanning all VM images:

```bash
$ curl -k \
  -u <USER> \
  H 'Content-Type: application/json' \
  -X POST \
  "https://<CONSOLE>/api/v<VERSION>/vms/stop"
```
