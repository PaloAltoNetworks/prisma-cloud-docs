Re-scans registry images.

The following example command forces Prisma Cloud Compute to re-scan all registry images:

## cURL Request

Refer to the following example cURL command that forces Prisma Cloud Compute to re-scan registry images:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>/api/v<VERSION>/registry/scan
```

Refer to the following example cURL command that forces Prisma Cloud Compute to re-scan a specific image:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"tag":{"registry":"<REGISTRY>","repo":"<REPO>","tag":"<TAG>","digest":""}}'\
  https://<CONSOLE>/api/v<VERSION>/registry/scan
```
