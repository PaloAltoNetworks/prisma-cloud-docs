This endpoint will kick off a scan of the any PCF Blobstores you have configured.

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/pcf-droplets/scan
```
