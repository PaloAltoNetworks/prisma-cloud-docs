Retrieves all audit events for file-integrity checks that are configured under host runtime rules.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/file-integrity"
```
### cURL Response

```
{
   "_id": "63762bc3b2a8e98a1c36a9e6",
   "eventType": "read",
   "path": "/etc/user/user",
   "fileType": 2,
   "processName": "cat",
   "user": "ubuntu",
   "time": "2022-11-17T12:40:35.046Z",
   "description": "Process cat read from path (user: ubuntu)",
   "hostname": "ip-172-31-9-109.ec2.internal",
   "fqdn": "",
   "ruleName": "user-host-arm",
   "accountID": "496947949261",
   "collections": [
     "All",
     "waas_oob_collection",
     "user123"
   ],
   "cluster": ""
}
...
...
...

```
