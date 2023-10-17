Returns the container Web-Application and API Security (WAAS) audit events data in CSV format. 

**Note:** These audit events relate to  violations of WAAS policies defined under **Defend > WAAS > Container > Container WAAS Policy**.

### cURL Request
Refer to the following example cURL command that downloads the WAAS container audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <waas-container-audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/container/download"
```
