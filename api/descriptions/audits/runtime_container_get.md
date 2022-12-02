Retrieves all container audit events when a runtime sensor such as process, network, file system, or system call detects an activity that deviates from the predictive model. 

**Note**: In Console, you can view the same under **Monitor > Events > Container Audits**.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/container"
```
### cURL Response

```
{
   "os": "Ubuntu 20.04.4 LTS",
   "_id": "636a952a5a293a6ea06cbb87",
   "time": "2022-11-08T17:43:06.68Z",
   "hostname": "jen-sle15-dock-0811t165158-cont-def-pre-lngcon230.c.twistlock-test-247119.internal",
   "fqdn": "",
   "user": "root",
   "type": "processes",
   "containerId": "6d5b5401b0e406ad064e7020b663236d0df177fa7f4a060c2f21262c27a4a6b2",
   "containerName": "/runtime-wf-base-alert",
   "imageName": "usertwistlock/ubuntu:wf-base",
   "imageId": "sha256:76913b92c0cbacbec7440a62d751c0a38aba1dde6aefe9e832d2a3aa0a3c3f9f",
   "effect": "alert",
   "ruleName": "sle15-container_alert_usertwistlock/ubuntu:wf-base_mqu",
   "msg": "/usr/bin/dash launched but is not found in the runtime model. Full command: /bin/sh -c sleep 3; curl http://169.254.169.254:80",
   "profileId": "sha256:76913b92c0cbacbec7440a62d751c0a38aba1dde6aefe9e832d2a3aa0a3c3f9f__",
   "interactive": true,
   "pid": 1955,
   "processPath": "/usr/bin/dash",
   "collections": [
     "All",
     "Prisma Cloud resources",
     "registry_scan_container_sle15-container_22_11_384_ghf",
     "sle15-container_alert_cnd"
   ],
   "attackType": "unexpectedProcess",
   "count": 1,
   "container": true,
   "severity": "high",
   "region": "us-central1-a",
   "accountID": "twistlock-test-247119",
   "attackTechniques": [
     "nativeBinaryExecution"
   ],
   "command": "/bin/sh -c sleep 3; curl http://169.254.169.253:80",
   "provider": "gcp"
 }
...
...
...

```