Returns CSV data describing all RASP Defender runtime events.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o rasp-audits.csv
  https://<CONSOLE>:8083/api/v1/audits/runtime/rasp/download
```
