Updates the compliance policy for running containers.
All rules in the policy are updated in a single shot.

This endpoint maps to the policy table in **Defend > Compliance > Containers and images > Deployed** in the Console UI.

To construct an effective rule for this policy, specify at least one "check" and one `effect` value. 
See [How to Construct a Compliance Policy](#how-to-construct-a-compliance-policy) for more info.

For a full list of checks, go to **Defend > Compliance > Containers and images > Deployed** in the Console UI and create a new rule.
All prebuilt checks and their IDs are shown under **Compliance actions**.

### cURL Request

Refer to the following example cURL command that overwrites all rules in your current policy with a new policy that has a single rule:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/compliance/container' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
  "rules":[
     {
       "name": "my-rule",
       "effect": "alert",
       "collections":[
         {
           "name":"All"
         }
       ],
       "condition": {
         "vulnerabilities": [
           {
             "id": 531,
             "block": false,
             "minSeverity": 1
           }
         ]
       }
     }
  ],
  "policyType":"containerCompliance"
}'
```

**Note:** No response will be returned upon successful execution.

