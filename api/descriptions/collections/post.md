Creates a new collection. You need to either specify a value or initialize the resouces in the endpoint with a "*" wildcard to be able to use the collection.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Collections and Tags > Collections**.
2. Add a collection using **+ Add collection**.
3. Click the **Save** button.

### cURL Request

Refer to the following example cURL command that creates a new collection named `my-collection`, specifies a HEX color value of #AD3C21, and captures all container images named `ubuntu:18.04`:

```bash
$ curl 'https://<CONSOLE>:8083/api/v<VERSION>/collections' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "name":"my-collection",
   "images":["ubuntu:18.04"],
   "hosts":["*"],
   "labels":["*"],
   "containers":["*"],
   "functions":["*"],
   "namespaces":["*"],
   "appIDs":["*"],
   "accountIDs":["*"],
   "codeRepos":["*"],
   "clusters":["*"], 
   "color":"#AD3C21"
}'
```
**Note:** Resources that are not explicitly specified need to have a `*` wildcard applied to them in order to instantiate as mentioned in the example.


