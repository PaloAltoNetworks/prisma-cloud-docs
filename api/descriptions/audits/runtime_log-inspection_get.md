Prisma Cloud Compute can provide audits for log inspection checks that are configured under host runtime rules.

The following example uses basic auth to list these audits:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/runtime/log-inspection
```

