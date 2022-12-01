Returns the trust audit events data in CSV format.


### cURL Request
Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <trust_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/trust/download"
```
