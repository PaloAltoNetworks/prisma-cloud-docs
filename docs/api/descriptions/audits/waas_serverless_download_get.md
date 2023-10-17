Returns the serverless function Web-Application and API Security (WAAS) audit events data in CSV format. 

**Note:** These are based on violations of WAAS policies defined under **Defend > WAAS > Serverless > Serverless WAAS Policy**.

### cURL Request

Refer to the following example cURL command that downloads the serverless WAAS audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <waas_serverless_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/serverless/download"

```

