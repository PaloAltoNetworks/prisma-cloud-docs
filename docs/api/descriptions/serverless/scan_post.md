Re-scan all serverless functions immediately.

### cURL Request

Refer to the following example cURL command that forces Prisma Cloud Compute to re-scan all serverless functions:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>/api/v<VERSION>/serverless/scan
```
