Re-scan all images immediately. This endpoint returns the time that the scans were initiated.

### cURL Request

Refer to the following example cURL command that forces Prisma Cloud Compute to re-scan all images:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>/api/v<VERSION>/images/scan
```
