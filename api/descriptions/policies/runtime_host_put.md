Updates the runtime policy for hosts protected by Defender.
All rules in the policy are updated in a single shot.

This endpoint maps to the **Add rule** button in **Defend > Runtime > Host policy** in the Console UI.

### cURL Request

Refer to the following example cURL command that overwrites all rules in your current policy with a new policy that has a single rule:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/runtime/host' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "rules":[
      {
         "name":"my-rule",
         "collections":[
            {
               "name":"All"       
            }
         ],
         "advancedProtection":"alert",
         "processes":{
            "effect":"alert"
         },
         "network":{
            "effect":"disable"
         },
         "dns":{
            "effect":"disable"
         }
      }
   ]
}'
```

**Note:** No response will be returned upon successful execution.
