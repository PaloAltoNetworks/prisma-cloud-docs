Updates the WAAS policy for web apps protected by App-Embedded Defender.
All rules in the policy are updated in a single shot.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > WAAS > App-Embedded**.
2. Click **+ Add rule** and enter the new rule information.
3. Click the **Add new app** button to move to the configuration window.
4. Configure the application with at least one endpoint, and click the **Save** button.

Adding and maintaining rules for a WAAS app involves populating a large and complex JSON request body.
We recommend the following process:

1. Manually define your app's policy via the Console UI as described [here](https://docs.twistlock.com/docs/compute_edition/waas/deploy_waas.html).
2. Use the **Export** button on **Defend** > **WAAS** to export the app's policy rules to a JSON file.
3. Use the exported file as a template to modify, then either import the file back in using the **Import** button, or use it as the basis for defining the rules to include in this endpoint's payload.

### cURL Request

The following cURL command overwrites all rules in your current policy with a new policy that has a single rule.

```bash
$ curl 'https://<CONSOLE>/api/v1/policies/firewall/app/app-embedded' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'
{
   "_id":"appEmbeddedAppFirewall",
   "rules":[
      {
         "name":"my-rule",
         "collections":[
            {
               "name":"All"
            }
         ],
         "applicationsSpec":[
            {
               "banDurationMinutes":5,
               "certificate":{
                  
               },
               "dosConfig":{
                  "effect":"disable",
                  "matchConditions":[
                     
                  ]
               },
               "apiSpec":{
                  "endpoints":[
                     {
                        "host":"*",
                        "basePath":"*",
                        "exposedPort":1,
                        "internalPort":1,
                        "tls":false,
                        "http2":false
                     }
                  ],
                  "paths":[
                     {
                        "path":"/api/v1/logs/system/upload",
                        "methods":[
                           {
                              "method":"POST"
                           }
                        ]
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
                  "effect":"prevent",
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
                  
               },
               "selected":true,
               "headerSpecs":[
                  
               ]
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
