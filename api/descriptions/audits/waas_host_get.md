Retrieves all host Web-Application and API Security (WAAS) audit events.

**Note:** These are based on violations of WAAS policies defined under **Defend > WAAS > Host > Host WAAS Policy**.

### cURL Request

Refer to the following example cURL command that retrieves all host WAAS audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/host"
```

### cURL Response

```
{
   "_id": "636ab7190487e34d5461a141",
   "profileId": "jen-rhe7-0811t164940-host-def-pre-lngcon230.c.twistlock-test-247119.internal",
   "time": "2022-11-08T20:07:53Z",
   "hostname": "jen-rhe7-0811t164940-host-def-pre-lngcon230.c.twistlock-test-247119.internal",
   "fqdn": "",
   "effect": "alert",
   "ruleName": "rhe7-host_22_11_384_host",
   "ruleAppID": "cggseacq",
   "msg": "Detected Local File Inclusion attack in request body, match ../, value ../../",
   "host": true,
   "containerName": "",
   "containerId": "",
   "imageName": "",
   "appID": "",
   "type": "lfi",
   "count": 1,
   "region": "us-central1-a",
   "version": "22.11.384",
   "accountID": "twistlock-test-247119",
   "url": "10.181.239.16:2001/",
   "userAgentHeader": "python-requests/2.27.1",
   "method": "POST",
   "urlPath": "/",
   "subnet": "10.180.30.249",
   "requestHeaders": "POST / HTTP/1.1\r\nHost: 10.181.239.16:2001\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nContent-Length: 6\r\nUser-Agent: python-requests/2.27.1\r\n",
   "requestHost": "10.181.239.16:2001",
   "requestHeaderNames": [
     "Accept",
     "Accept-Encoding",
     "Connection",
     "Content-Length",
     "User-Agent"
   ],
   "responseHeaderNames": [
     "Content-Length",
     "Content-Type",
     "Date",
     "Server"
   ],
   "statusCode": 404,
   "collections": [
     "All",
     "rhe7-host_mhm",
     "compliance_rhe7_hhk",
     "waas_collection_host_rhe7-host_22_11_384_hpx"
   ],
   "resource": {
     "hosts": [
       "jen-rhe7-0811t164940-host-def-pre-lngcon230.c.twistlock-test-247119.internal"
     ],
     "accountIDs": [
       "twistlock-test-247119"
     ]
   },
   "attackTechniques": [
     "exploitPublicFacingApplication",
     "applicationExploitRCE"
   ],
   "protection": "firewall",
   "attackField": {
     "value": "../../",
     "type": "rawBody"
   },
   "eventID": "306032c4-2175-6d95-7a2c-c9abacfc9cb6",
   "provider": "gcp"
 }

```

