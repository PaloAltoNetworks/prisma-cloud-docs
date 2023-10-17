Returns all app-embedded WAAS audit events for the specified query parameters.

**Note:** These audit events relate to  violations of WAAS policies defined under **Defend > WAAS > App-Embedded > App-Embedded WAAS Policy**.

### cURL Request
Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/app-embedded"
```
### cURL Response

```
{
   "_id": "636ab72055e55c25de4702c3",
   "time": "2022-11-08T20:08:00Z",
   "hostname": "waas-mock-service-testing:24edfabfc76140ae97485844b0d7579c",
   "fqdn": "",
   "effect": "alert",
   "ruleName": "waas-mock-service-testing_22_11_384_fargate",
   "ruleAppID": "hxrbsrky",
   "msg": "Detected Local File Inclusion attack in request body, match ../, value ../../",
   "host": true,
   "containerName": "",
   "containerId": "",
   "imageName": "",
   "appID": "waas-mock-service-testing:24edfabfc76140ae97485844b0d7579c",
   "type": "lfi",
   "count": 1,
   "region": "us-east-1",
   "version": "22.11.384",
   "accountID": "496947949261",
   "url": "34.239.179.111:2001/",
   "userAgentHeader": "python-requests/2.27.1",
   "method": "POST",
   "urlPath": "/",
   "subnet": "34.72.93.22",
   "requestHeaders": "POST / HTTP/1.1\r\nHost: 34.239.179.111:2001\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nContent-Length: 6\r\nUser-Agent: python-requests/2.27.1\r\n",
   "requestHost": "34.239.179.111:2001",
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
     "waas_collection_fargate_waas-mock-service-testing_22_11_384_zxo"
   ],
   "resource": {
     "appIDs": [
       "waas-mock-service-testing:24edfabfc76140ae97485844b0d7579c"
     ],
     "accountIDs": [
       "496947949261"
     ]
   },
   "cluster": "automation-fargate-test",
   "attackTechniques": [
     "exploitPublicFacingApplication",
     "applicationExploitRCE"
   ],
   "protection": "firewall",
   "attackField": {
     "value": "../../",
     "type": "rawBody"
   },
   "eventID": "8513bd5f-3091-06cf-b856-4d007f11443d",
   "provider": "aws"
 }

```
