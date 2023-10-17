Updates the WAAS policy for serverless functions.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > WAAS > Serverless** page.
2. Click **+ Add rule**.
3. Enter the details for the new serverless function and click **Save**

Adding and maintaining rules for a WAAS app involves populating a large and complex JSON request body.
We recommend the process:

1. Manually define your app's policy via the Console UI as described [here](https://docs.twistlock.com/docs/compute_edition/waas/deploy_waas.html).
2. Use the **Export** button on **Defend** > **WAAS** to export the app's policy rules to a JSON file.
3. Use the exported file as a template to modify, then either import the file back in using the **Import** button, or use it as the basis for defining the rules to include in this endpoint's payload.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/serverless' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
  "_id": "serverlessAppFirewall",
  "rules": [
    {
      "name": "{id}",
      "previousName": "",
      "collections": [
        {
          "hosts": ["*"],
          "images": ["*"],
          "labels": ["*"],
          "containers": ["*"],
          "functions": ["*"],
          "namespaces": ["*"],
          "appIDs": ["*"],
          "accountIDs": ["*"],
          "codeRepos": ["*"],
          "clusters": ["*"],
          "name": "All"
        }
      ],
      "applicationsSpec": [
        {
          "xss": {
            "effect": "alert",
            "exceptionFields": []
          },
          "codeInjection": {
            "effect": "alert",
            "exceptionFields": []
          },
          "sqli": {
            "effect": "alert",
            "exceptionFields": []
          },
          "lfi": {
            "effect": "alert",
            "exceptionFields": []
          },
          "cmdi": {
            "effect": "alert",
            "exceptionFields": []
          },
          "body": {
            "inspectionSizeBytes": 131072
          }
        }
      ]
    }
  ],
  "minPort": 0,
  "maxPort": 0
}'
```

​**Note:** No response will be returned upon successful execution.
