Returns the agentless Web-Application and API Security (WAAS) audit events data in CSV format. 

**Note:** These are based on violations of WAAS policies defined under **Defend > WAAS > Agentless > Agentless WAAS Policy**.

### cURL Request

Refer to the following example cURL command that retrieves all agentless WAAS audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <waas_agentless_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/agentless/download"
```