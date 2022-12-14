Returns the management audit events data in CSV format. 

Management audits are:
* Changes to any settings (including previous and new values)
* Changes to any rules (create, modify, or delete)
* Logon activities (success and failure)

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <mgmt_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/mgmt/download"
```
