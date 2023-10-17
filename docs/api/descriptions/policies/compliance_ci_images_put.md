Updates the compliance policy for images scanned in your continuous integration (CI) pipeline.
All rules in the policy are updated in a single shot.

The policy set in this endpoint is enforced by the scanners in the Jenkins plugin and the `twistcli` command line tool.

This endpoint maps to the policy table in **Defend > Compliance > Containers and images > CI** in the Console UI.


### cURL Request

The following cURL command overwrites all rules in your current policy with a new policy that has a single rule.

To construct an effective rule for this policy, specify at least one "check" and the `effect`.
See [How to Construct a Compliance Policy](#how-to-construct-a-compliance-policy) for more info.

For a full list of checks, go to **Defend > Compliance > Containers and images > CI** in the Console UI and create a new rule.
All prebuilt checks and their IDs are shown under **Compliance actions**.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/compliance/ci/images' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
  "rules": [
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
         			"id": 41,
         			"block": false,
         			"minSeverity": 1
         		}
         	]
      }
    }
  ],
  "policyType": "ciImagesCompliance"
}'
```

**Note:** No response will be returned upon successful execution.



