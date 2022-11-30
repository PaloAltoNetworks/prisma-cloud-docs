Retrieves all Cloud Native Network Segmentation (CNNS) host audits.

For hosts, rules are defined between:
* Host to host.
* Host to an external network not protected by Prisma Cloud

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/network/host"
```

### cURL Response

```
{
   "_id": "john-photon-v3-0811t165011-host-def-pre-lngcon230",
   "time": "2022-11-08T20:22:52.207Z",
   "total": 4,
   "resource": {
     "hosts": [
       "john-cen8-cons-dock-0811t160649-cons-ssugandh-lngcon230.c.twistlock-test-247119.internal",
       "john-photon-v3-0811t165011-host-def-pre-lngcon230"
     ],
     "accountIDs": [
       "twistlock-test-247119"
     ]
   },
   "collections": [
     "All",
     "registry_scan_container_cen8-container_22_11_384_piu",
     "photon-v3-host_crn",
     "compliance_photon_etz",
     "cnnf_cen8_client_itu",
     "cnnf_photon_server_fsr"
   ],
   "audits": {
     "unexpectedConnection": {
       "count": 4,
       "audits": [
         {
           "ruleID": 15,
           "time": "2022-11-08T20:22:52.207Z",
           "type": "unexpectedConnection",
           "srcHostname": "john-cen8-cons-dock-0811t160649-cons-ssugandh-lngcon230.c.twistlock-test-247119.internal",
           "dstHostname": "john-photon-v3-0811t165011-host-def-pre-lngcon230",
           "dstPort": 80,
           "block": false,
           "count": 1,
           "accountID": "twistlock-test-247119"
         },
         {
           "ruleID": 15,
           "time": "2022-11-08T20:22:48.175Z",
           "type": "unexpectedConnection",
           "srcHostname": "john-cen8-cons-dock-0811t160649-cons-ssugandh-lngcon230.c.twistlock-test-247119.internal",
           "dstHostname": "john-photon-v3-0811t165011-host-def-pre-lngcon230",
           "dstPort": 80,
           "block": false,
           "count": 1,
           "accountID": "twistlock-test-247119"
         },
         {
           "ruleID": 15,
           "time": "2022-11-08T20:22:46.127Z",
           "type": "unexpectedConnection",
           "srcHostname": "john-cen8-cons-dock-0811t160649-cons-ssugandh-lngcon230.c.twistlock-test-247119.internal",
           "dstHostname": "john-photon-v3-0811t165011-host-def-pre-lngcon230",
           "dstPort": 80,
           "block": false,
           "count": 1,
           "accountID": "twistlock-test-247119"
         },
         {
           "ruleID": 15,
           "time": "2022-11-08T20:22:45.122Z",
           "type": "unexpectedConnection",
           "srcHostname": "john-cen8-cons-dock-0811t160649-cons-ssugandh-lngcon230.c.twistlock-test-247119.internal",
           "dstHostname": "john-photon-v3-0811t165011-host-def-pre-lngcon230",
           "dstPort": 80,
           "block": false,
           "count": 1,
           "accountID": "twistlock-test-247119"
         }
       ]
     }
   }
 }

```