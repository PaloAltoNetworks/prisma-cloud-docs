Returns the audit events data in CSV format for log inspection checks that are configured under host runtime rules.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <runtime_log-inspection_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/incidents/runtime/log-inspection/download"
```

