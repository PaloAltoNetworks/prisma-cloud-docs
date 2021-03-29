Downloads the runtime host audit logs in CSV format.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o host_audits.csv \
  https://<CONSOLE>:8083/api/v1/audits/runtime/host/download
```

