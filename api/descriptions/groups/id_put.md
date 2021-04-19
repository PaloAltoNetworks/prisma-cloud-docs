Creates or modifies a group.
The `id` can be retrieved with from the `GET /api/v1/groups` endpoint.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Groups**.
2. Click the row of the group you want to update or click dotted icon under the **Actions** column to open the menu options and click the **Manage** button.
3. Update the group's parameters. 
4. Click the **Save** button to save the changes.

### cURL Request

The PUT cURL command updates a group.

**To submit a cURL request:**

* The `name` value is required.
* If one of the following resources is left unspecified, the resource value will be set to a wildcard `[*]`: `hosts`, `images`, `labels`, `containers`, `functions`, `namespaces`, `appIDs`, `accountIDs`, `codeRepos`, `clusters`

The following cURL command updates `my-group` with the users associated with the usernames `john` and `jane`.

**Note:** You can retrieve the group `id` names from the `GET /api/v1/groups`.

```bash
$ curl 'https://<CONSOLE>/api/v1/groups/{id}' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "groupName": "my-group",
   "user": [
   		{"username": "john"},
   		{"username": "jane"}
   	],
   	"lastModified":"2021-03-11T23:32:51.336Z"
}'
```

You must include a `lastModified` timestamp even though it will be overwritten by the system

**Note:** No response will be returned upon successful execution.
