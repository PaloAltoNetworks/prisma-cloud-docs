Updates the list of rules that make up your trusted images policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \ 
'{
   "_id":"imageTrust",
   "rules":[{"allowedGroups":[],"deniedGroups":[],
   "effect":"alert","action":["*"],
   "blockMsg":"",
   "resources":{"images":["*"],"hosts":["*"],"labels":["*"]},
   "name":"My rule"}]
}' \
  https://<CONSOLE>:8083/api/v1/policies/trust
```
