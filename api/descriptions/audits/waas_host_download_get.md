Returns the host Web-Application and API Security (WAAS) audit events data in CSV format. 

**Note:** These audit events relate to violations of WAAS policies defined under **Defend > WAAS > Host > Host WAAS Policy**.

### cURL Request

Refer to the following example cURL command that downloads the host WAAS audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <waas-host-audits.csv> \
  "https://console:8083/api/v1/audits/firewall/app/host/download"
```