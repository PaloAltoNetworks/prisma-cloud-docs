Creates a new collection.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Collections and Tags > Collections**.
2. Add a collection using **+ Add collection**.
3. Click the **Save** button.

### cURL Request

Refer to the following example cURL command that creates a new collection named `my-collection` and captures all container images named `ubuntu:18.04`:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/collections' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "name":"my-collection",
   "images":["ubuntu:18.04"]
}'
```
Any resource left unspecified, such as `hosts`, `functions`, or `clusters`, is assigned a wildcard by default.
Resources that are not explicitly specified need to have a `*` wildcard applied to them in order to instantiate.


