Updates the WAAS policy for hosts.
All rules in the policy are updated in a single shot.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > WAAS > Host**.
2. Click **+ Add rule** and enter the new rule information.
3. Click the **Add new app** button to move to the configuration window.
4. Configure the application with at least one endpoint, and click the **Save** button.

Adding and maintaining rules for a WAAS app involves populating a large and complex JSON request body.
We recommend the following process:

1. Manually define your app's policy via the Console UI as described [here](https://docs.twistlock.com/docs/compute_edition/waas/deploy_waas.html).
2. Use the **Export** button on **Defend** > **WAAS** to export the app's policy rules to a JSON file.
3. Use the exported file as a template to modify, then either import the file back in using the **Import** button, or use it as the basis for defining the rules to include in this endpoint's payload.

### cURL Request

Refer to the following example cURL command that overwrites all rules in your current policy with a new policy that has a single rule:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/host' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "_id":"hostAppFirewall",
   "rules":[
      {
         "name":"My Rule",
         "notes":"My Notes 4",
         "collections":[
            {
               "name":"All"
            }
         ],
         "applicationsSpec":[
            {
               "banDurationMinutes":5,
               "certificate":{
                  "encrypted":""
               },
               "dosConfig":{
                  "effect":"disable"
               },
               "apiSpec":{
                  "description":"test",
                  "endpoints":[
                     {
                        "host":"*",
                        "basePath":"*",
                        "exposedPort":0,
                        "internalPort":1,
                        "tls":false,
                        "http2":false
                     }
                  ],
                  "effect":"disable",
                  "fallbackEffect":"disable"
               },
               "botProtectionSpec":{
                  "userDefinedBots":[
                     
                  ],
                  "knownBotProtectionsSpec":{
                     "searchEngineCrawlers":"disable",
                     "businessAnalytics":"disable",
                     "educational":"disable",
                     "news":"disable",
                     "financial":"disable",
                     "contentFeedClients":"disable",
                     "archiving":"disable",
                     "careerSearch":"disable",
                     "mediaSearch":"disable"
                  },
                  "unknownBotProtectionSpec":{
                     "generic":"disable",
                     "webAutomationTools":"disable",
                     "webScrapers":"disable",
                     "apiLibraries":"disable",
                     "httpLibraries":"disable",
                     "botImpersonation":"disable",
                     "browserImpersonation":"disable",
                     "requestAnomalies":{
                        "threshold":9,
                        "effect":"disable"
                     }
                  },
                  "sessionValidation":"disable",
                  "interstitialPage":false,
                  "jsInjectionSpec":{
                     "enabled":false,
                     "timeoutEffect":"disable"
                  }
               },
               "networkControls":{
                  "advancedProtectionEffect":"alert",
                  "deniedSubnetsEffect":"alert",
                  "deniedCountriesEffect":"alert",
                  "allowedCountriesEffect":"alert"
               },
               "body":{
                  "inspectionSizeBytes":131072
               },
               "intelGathering":{
                  "infoLeakageEffect":"disable",
                  "removeFingerprintsEnabled":true
               },
               "maliciousUpload":{
                  "effect":"disable",
                  "allowedFileTypes":[                     
                  ],
                  "allowedExtensions":[                     
                  ]
               },
               "csrfEnabled":true,
               "clickjackingEnabled":true,
               "sqli":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "xss":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "attackTools":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "shellshock":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "malformedReq":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "cmdi":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "lfi":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "codeInjection":{
                  "effect":"alert",
                  "exceptionFields":[                     
                  ]
               },
               "remoteHostForwarding":{                  
               }
            }
         ],
         "expandDetails":true
      }
   ],
   "minPort":30000,
   "maxPort":31000
}'
```

**Note:** No response will be returned upon successful execution.
