Download all docker access audits into a CSV format file.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/access/download?type=docker > aqsa_audits.csv
```
