Adds a runtime policy for app-embedded deployments.

This endpoint maps to the **Add rule** button in **Defend > Runtime > App-Embedded policy** in the Console UI.

### cURL Request

The following cURL command adds a single rule to your policy.

```bash
$ curl 'https://<CONSOLE>/api/v1/policies/runtime/app-embedded' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
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
       "effect":"alert",
       "blacklistIPs":[               
       ],
       "blacklistListeningPorts":[               
       ],
       "whitelistListeningPorts":[
       ],
       "blacklistOutboundPorts":[               
       ],
       "whitelistOutboundPorts":[
          {
             "start":4312,
             "end":4555,
             "deny":false
          }
       ],
       "whitelistIPs":[               
       ]
    },
    "dns":{
       "effect":"prevent",
       "whitelist":[
       ],
       "blacklist":[               
       ]
    }
}'
```

**Note:** No response will be returned upon successful execution.
