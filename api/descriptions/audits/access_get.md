Retrieves all docker access audit events that are logged and aggregated for any container resource protected by a Defender in Prisma Cloud Compute.

You can configure Prisma Cloud Compute to log and aggregate events such as sudo and SSH access on hosts protected by Defender. These events create an audit trail that tracks system components accessed by individual users. 

**Note**: Access events can also be viewed in Console under **Monitor > Events > Docker audits**.

### cURL Request
Refer to the following example cURL command that gives a list of all access audit events:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/access"
```
### cURL response
```
[
 {
   "containerName": "/compliance_block_container_photon_fua",
   "imageName": "alpine:latest",
   "user": "",
   "type": "docker",
   "time": "2022-11-08T18:24:09.249Z",
   "hostname": "jen-photon-v3-0811t165215-cont-def-pre-lngcon230",
   "fqdn": "",
   "sourceIP": "",
   "allow": false,
   "ruleName": "compliance_block_container_rule_svn",
   "api": "create",
   "msg": "[Twistlock] Container operation blocked by policy: compliance_block_container_rule_svn, has 1 compliance issues ",
   "collections": [
     "All",
     "compliance_block_container_yue"
   ],
   "accountID": "twistlock-test-123456",
   "cluster": "",
   "namespace": ""
 }
 ...
]

```
Refer to the following example cURL command that gives a list of only docker type access audit events: 

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/audits/access?type=docker

```
