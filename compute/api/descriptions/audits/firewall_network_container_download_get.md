Downloads all network firewall audits (CNNF) into a CSV file.  

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o cnnf_container_audits.csv \
  https://<CONSOLE>:8083/api/v1/audits/firewall/network/container/download
```
