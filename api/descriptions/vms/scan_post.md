Re-scans all VM images immediately. This endpoint returns the time that the scans were initiated.

### cURL Request

Refer to the following example cURL command that forces Prisma Cloud to re-scan all VM images:

```bash
$ curl -k \
  -u <USER> \
  H 'Content-Type: application/json' \
  -X POST \
  "https://<CONSOLE>/api/v<VERSION>/vms/scan"
```
