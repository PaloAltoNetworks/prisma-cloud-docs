Creates a new collection. You must specify a value for mandatory resources such as 'name', 'images', and 'labels' in the collection.

For 'name': Valid characters are 'A-Z', 'a-z', '0-9', '_', '-', and ':'.
For 'image': If you don't have a specific value, you can initialize with a wildcard '*'.
For 'label': If you don't have a specific value, you can initialize with a wildcard '*'.

Values for the mandatory resources are required for initialization. If you don't initialize mandatory resources and try to use the collection, you'll get an empty resource error.

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
**Note:** No response is returned upon successful execution. You must verify the collection in the Console UI.


