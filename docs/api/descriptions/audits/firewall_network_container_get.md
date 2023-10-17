Retrieves all Cloud Native Network Segmentation (CNNS) container audit events.

For more information, see the [Cloud Native Network Segmentation (CNNS)](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/firewalls/cnns_saas)

For containers, rules are defined between:
* Image to image.
* Image to an external network not protected by Prisma Cloud.
* Image to DNS domain.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/network/container"
```

### cURL Response

```
{
   "_id": "localhost",
   "time": "2022-11-14T11:02:43.151Z",
   "total": 1,
   "resource": {
     "images": [
       ""
     ]
   },
   "collections": [
     "All",
     "user123"
   ],
   "audits": {
     "unexpectedConnection": {
       "count": 1,
       "audits": [
         {
           "ruleID": 4,
           "time": "2022-11-14T11:02:43.151Z",
           "type": "unexpectedConnection",
           "srcProfileID": "sha256:8d5df41c547bd107c14368ad302efc46760940ae188df451cabc23e10f7f161b_user_tkgi-users",
           "dstProfileID": "20",
           "srcProfileHash": 228,
           "srcContainerName": "users-ubuntu",
           "dstContainerName": "",
           "dstSubnet": "localhost",
           "srcImageName": "docker.io/library/ubuntu:18.04",
           "dstImageName": "",
           "dstPort": 8000,
           "block": false,
           "count": 1,
           "msg": "Unexpected connection to ip 127.0.0.1"
         }
       ]
     }
   }
 }

```
