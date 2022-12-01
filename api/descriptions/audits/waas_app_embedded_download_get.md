Returns the app-embedded WAAS audit events data in CSV format for the specified query parameters.

**Note:** These audit events relate to  violations of WAAS policies defined under **Defend > WAAS > App-Embedded > App-Embedded WAAS Policy**.

### cURL Request
Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <waas_app-embedded_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/app-embedded/download"
```
