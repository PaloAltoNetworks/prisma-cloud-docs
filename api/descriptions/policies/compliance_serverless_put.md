Updates the rules that make up your compliance policy for functions.  

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{
  "rules": [
    {
      "name": "Default - Alert",
      "effect": "alert",
      "resources": {
        "functions": [
          "*"
        ]
      },
      "condition": {
        "readonly": false,
        "device": "",
        "vulnerabilities": [
          {
            "id": 434,
            "block": false,
            "minSeverity": 0
          },
          {
            "id": 435,
            "block": false,
            "minSeverity": 0
          },
          {
            "id": 436,
            "block": false,
            "minSeverity": 0
          },
        ]
      },
      "alertThreshold": {
        "disabled": false,
        "value": 0
      },
      "blockThreshold": {
        "enabled": false,
        "value": 0
      },
      "graceDays": 0
    }
  ],
  "policyType": "serverlessCompliance",
  "_id": "serverlessCompliance"
}'
  https://<CONSOLE>:8083/api/v1/policies/compliance/serverless
```
