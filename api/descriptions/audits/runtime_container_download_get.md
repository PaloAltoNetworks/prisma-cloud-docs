Downloads the runtime container audit logs in CSV format.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/runtime/container/download
  > container_audits.csv
```
