Returns the access admission events data in CSV format that were alerted or blocked by Defender functioning as Open Policy Agent admission controller.

### cURL Request
Refer to the following example cURL command that downloads the admission audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <admission_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/admission/download"

```