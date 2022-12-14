Returns the audit events data in CSV format for file-integrity checks that are configured under host runtime rules.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o <runtime_file-integrity_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/file-integrity/download"
```