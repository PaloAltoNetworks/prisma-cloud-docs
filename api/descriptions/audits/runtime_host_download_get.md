Returns the runtime host audit events data in CSV format.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <runtime_host_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/host/download"
```

