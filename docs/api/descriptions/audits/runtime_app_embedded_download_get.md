Returns the app-embedded runtime audit events data in CSV format.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <runtime_app-embedded_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/app-embedded/download"
```
