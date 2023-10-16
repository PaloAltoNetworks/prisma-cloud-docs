Updates the runtime policy for your serverless functions.
All rules in the policy are updated in a single shot.

This endpoint maps to the **Add rule** button in **Defend > Runtime > Serverless policy** in the Console UI.

### cURL Request

Refer to the following example cURL command that overwrites all rules in your current policy with a new policy that has a single rule:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/runtime/serverless' \
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
         "processes":{
            "effect":"alert"
         },
         "network":{
            "effect":"disable"
         },
         "dns":{
            "effect":"disable"
         },
         "filesystem":{
            "effect":"disable"
         }
      }
   ]
}'
```

**Note:** No response will be returned upon successful execution.
