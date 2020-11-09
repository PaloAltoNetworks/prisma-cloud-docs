Re-scan registry images immediately.

The following example command forces Twistlock to re-scan all registry images:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/registry/scan
```

The following example command forces Twistlock to re-scan a specific image:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  -d '{"tag":{"registry":"<REGISTRY>","repo":"<REPO>","tag":"<TAG>","digest":""}}'\
  https://<CONSOLE>:8083/api/v1/registry/scan
```
