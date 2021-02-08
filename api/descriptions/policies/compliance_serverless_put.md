Updates the compliance policy for serverless functions situated in your cloud provider's infrastructure.
All rules in the policy are updated in a single shot.

This endpoint maps to the policy table in **Defend > Compliance > Functions > Functions** in the Console UI.

### cURL Request

The following cURL command overwrites all rules in your current policy with a new policy that has a single rule.

To construct an effective rule for this policy, specify at least one "check" and one `effect` value. 
See [How to Construct a Compliance Policy](#how-to-construct-a-compliance-policy) for more info.

For a full list of checks, go to **Defend > Compliance > Functions > Functions** in the Console UI and create a new rule.
All prebuilt checks and their IDs are shown under **Compliance actions**.

```bash
$ curl 'https://<CONSOLE>/api/v1/policies/compliance/serverless' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "rules":[
      {
         "name":"my-rule",
         "effect":"alert",
         "collections":[
            {
               "name":"All"
            }
         ],
         "condition":{
            "vulnerabilities":[
               {
                  "id":434,
                  "block":false
               }
            ]
         }
      }
   ],
   "policyType":"serverlessCompliance"
}'
```

**Note:** No response will be returned upon successful execution.

