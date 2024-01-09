Creates a new collection. Only the `name` field is required; the other fields are optional. The `name` field can contain the characters: 'A-Z', 'a-z', '0-9', '_', '-', and ':'. Optional fields for which you do not specify a value are set to the '*' wildcard.

If you don't provide a value for the `name` field and try to use the collection, you'll get an empty resource error.

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


