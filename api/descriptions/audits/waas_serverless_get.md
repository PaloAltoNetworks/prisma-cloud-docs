Retrieves all serverless function Web-Application and API Security (WAAS) audit events.

**Note:** These are based on violations of WAAS policies defined under **Defend > WAAS > Serverless > Serverless WAAS Policy**.

### cURL Request

Refer to the following example cURL command that retrieves all serverless WAAS audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/serverless"
```

### cURL Response

```
{
        "_id": "",
        "time": "0001-01-01T00:00:00Z",
        "hostname": "",
        "fqdn": "",
        "effect": "",
        "ruleName": "",
        "ruleAppID": "",
        "msg": "",
        "host": false,
        "containerName": "",
        "containerId": "",
        "imageName": "",
        "appID": "",
        "type": "cmdi",
        "count": 1,
        "url": "",
        "subnet": "",
        "requestHeaders": "",
        "attackField": {},
        "eventID": ""
}

```

