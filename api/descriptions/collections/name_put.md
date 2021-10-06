Updates the parameters for a specific collection.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Collections and Tags > Collections**.
2. Click the dotted icon under the **Actions** column to open up the menu options. **Note:** The default collections do not have a dotted icon in the **Actions** column. Use the  **Manage** cog icon to open the update window.
3. Click the **Manage** button and update the collection's parameters. 
4. Click the **Save** button to save the changes.

### cURL Request

The PUT cURL command updates a collection.

**To submit a cURL request:**

* The `name` value is required.
* If `description` is not included in the request, the value will be defaulted to an empty string.
* If `color` is not included in the request, the system will set the color to a random value.
* If one of the following resources is left unspecified, the resource value will be set to a wildcard `[*]`: `hosts`, `images`, `labels`, `containers`, `functions`, `namespaces`, `appIDs`, `accountIDs`, `codeRepos`, `clusters`

#### Example cURL Request

This existing collection `my-collection` captures all container images named `ubuntu:18.04`.

```json
{
   "hosts":["*"],
   "images":["ubuntu:18.04"],
   "labels":["*"],
   "containers":["*"],
   "functions":["*"],
   "namespaces":["*"],
   "appIDs":["*"],
   "accountIDs":["*"],
   "codeRepos":["*"],
   "clusters":["*"],
   "name":"my-collection",
   "owner":"<OWNER_NAME>",
   "modified":"2021-01-01T21:04:30.417Z",
   "color":"#AD3C21",
   "system":"false"
}
```

The following cURL command updates `my-collection` to captures all container images named `ubuntu:20.04`.

**Note:** You can retrieve collection names from the `GET /api/v<VERSION>/collections` endpoint using the `name` key.

Refer to the following example cURL command:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/collections/my-collection' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "name":"my-collection",
   "images":["ubuntu:20.04"]
}'
```

**Note:** No response will be returned upon successful execution.
