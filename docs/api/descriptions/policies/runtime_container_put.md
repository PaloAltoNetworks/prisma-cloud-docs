Updates the runtime policy for containers.
All rules in the policy are updated in a single shot.

Prisma Cloud automatically builds allow-list security models for each container image in your environment.
Use runtime container rules to augment the rules in those models.
Manually defined rules augment learned models as follows:

Policy (allowed) = Manual rules (explicitly allowed) + Model (all learned behavior) - Manual rules (explicitly denied)

This endpoint maps to the **Add rule** button in **Defend > Runtime > Container policy** in the Console UI.

### cURL Request

Refer to the following example cURL command that overwrites all rules in your current policy with a new policy that has a single rule:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/runtime/container' \
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
            "effect":"alert"
         },
         "dns":{
            "effect":"alert"
         },
         "filesystem":{
            "effect":"alert"
         }
      }
   ]
}'
```

**Note:** No response will be returned upon successful execution.
