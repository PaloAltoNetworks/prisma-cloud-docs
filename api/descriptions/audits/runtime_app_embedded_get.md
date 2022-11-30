Retrieves all app-embedded runtime audit events.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/app-embedded"
```

### cURL Response

```
{
   "_id": "636be11d2408ed63b48ebd44",
   "time": "2022-11-09T17:19:25.12Z",
   "hostname": "automation_azure_presetup-prevent-tvzwx:aa9f944f-0456-004d-7c69-fd444591fefd",
   "fqdn": "",
   "user": "root",
   "type": "network",
   "imageName": "automation_azure_presetup-prevent-tvzwx",
   "imageId": "b446aac9-6ee0-f254-ff75-cb21755cebdb",
   "effect": "prevent",
   "ruleName": "automation_azure_presetup-prevent-tvzwx_wul",
   "msg": "DNS resolution of domain name SandboxHost-638036111205626034 triggered by /usr/local/bin/python3.9 explicitly denied by a runtime rule",
   "profileId": "automation_azure_presetup-prevent-tvzwx:aa9f944f-0456-004d-7c69-fd444591fefd_",
   "pid": 28,
   "processPath": "/usr/local/bin/python3.9",
   "collections": [
     "All",
     "automation_azure_presetup-prevent-tvzwx_dde"
   ],
   "attackType": "explicitlyDeniedDNS",
   "count": 1,
   "severity": "high",
   "appID": "automation_azure_presetup-prevent-tvzwx:aa9f944f-0456-004d-7c69-fd444591fefd",
   "version": "22.11.384",
   "accountID": "Non-onboarded cloud accounts"
}
...
...
...

```
