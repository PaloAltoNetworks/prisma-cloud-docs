Downloads the runtime host audit logs in csv format.

A call to this api endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o host_audits.csv \
  https://<CONSOLE>:8083/api/v1/audits/runtime/host/download
```

