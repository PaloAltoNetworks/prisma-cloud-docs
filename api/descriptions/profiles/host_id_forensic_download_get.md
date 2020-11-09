Downloads the forensic data for a host, which can be used to investigate runtime incidents.


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/cvs' \
  -X GET \
  -o host_forensic.csv
  "https://<CONSOLE>:8083/api/v1/profiles/host/{id}/forensic/download"
```
