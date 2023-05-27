Scans the TAS Droplets.

### cURL Request

Refer to the following cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/tas-droplets/scan"
```