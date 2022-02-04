Stops current registry scan immediately.

## cURL Request

Refer to the following example cURL command that forces Prisma Cloud Compute to stop scanning all registry images:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>/api/v<VERSION>/registry/stop
```
