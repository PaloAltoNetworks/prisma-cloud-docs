Creates a tag that helps you manage the vulnerabilities in your environment. 
You can use tags as policy exceptions or assign them to vulnerabilities for action.

**Note:** `""` (an empty string) is automatically assigned for any unspecified field.

### cURL Request

Refer to the following example cURL command that creates a tag named "my-tag":

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "name": "my-tag",
   "color": "#ff0000",
   "description": "A test collection"
 }' \
  "https://<CONSOLE>/api/v<VERSION>/tags"
```
