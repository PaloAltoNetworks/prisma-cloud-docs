Creates a new collection.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Collections and Tags > Collections**.
2. Add a collection using **+ Add collection**.
3. Click the **Save** button.

### cURL Request

The following cURL command creates a new collection named `my-collection`.
This collection captures all container images named `ubuntu:18.04`.
Any resource left unspecified, such as `hosts`, `functions`, and `clusters`, is assigned a wildcard by default.

```bash
$ curl 'https://<CONSOLE>/api/v1/collections' \
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

**Note:** No response will be returned upon successful execution.
