Retrieves the runtime host audit events.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/host"
```
### cURL Response

```
{
   "_id": "637628beb2a8e98a1c36a9e1",
   "time": "2022-11-17T12:27:42.003Z",
   "hostname": "ip-172-31-9-109.ec2.internal",
   "fqdn": "",
   "type": "network",
   "effect": "alert",
   "ruleName": "user-host-arm",
   "msg": "DNS resolution of name www.yahoo.com, type AAAA explicitly denied by a runtime rule",
   "profileId": "ip-172-31-9-109.ec2.internal",
   "collections": [
     "All",
     "waas_oob_collection",
     "user123"
   ],
   "attackType": "explicitlyDeniedDNS",
   "count": 1,
   "severity": "high",
   "region": "us-east-1",
   "accountID": "496947949261",
   "domain": "www.yahoo.com",
   "provider": "aws",
   "resourceID": "i-0bc31d26963bd2933"
}
...
...
...

```