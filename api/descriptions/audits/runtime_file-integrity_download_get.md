Twistlock can provide audits for file-integrity checks that are configured under host runtime rules.

The following example uses basic auth to download these audits:


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o file-integrity-events.csv \
  https://console:8083/api/v1/audits/runtime/file-integrity/download
```

