Downloads all CNAF firewall audits for RASP Defenders into a CSV file.  

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o rasp_cnaf_audits.csv \
  https://console:8083/api/v1/audits/firewall/app/rasp/download
```

