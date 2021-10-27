Prisma Cloud Compute can provide audits for log inspection checks that are configured under host runtime rules.

The following example uses basic auth to download these audits:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o log-inspection.csv \
  https://console:8083/api/v1/audits/incidents/runtime/log-inspection/download
```

