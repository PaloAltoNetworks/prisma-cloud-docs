Updates the list of CNNF network objects.

The following example curl command updates the network objects.  There is an example of all three types (images,subnets, and applications ):

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \
'[
   {"_id":"Ubuntu","type":"container","resource":{"images":["ubuntu:latest"],"labels":["*"]}},
   {"_id":"Google DNS","type":"subnet","resource":{"labels":["*"]},"subnets":[{"name":"8.8.8.8/24","cidr":"8.8.8.8/24"}]},
   {"_id":"SSH","type":"appID","resource":{"appIDs":["ssh"]},"subnets":[]}
]' \
  https://<CONSOLE>:8083/api/v1/policies/firewall/network/entities
```
