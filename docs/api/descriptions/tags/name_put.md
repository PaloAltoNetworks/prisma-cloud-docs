Updates the parameters in a given tag.

You must define all parameters in your PUT request.

**Note:** `""` (an empty string) is automatically assigned for any unspecified field.

### cURL Request

Refer to the following example cURL command that updates the parameters in a tag named `my_tag`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \
'{
   "name": "my_tag2",
   "color": "#ff0000",
   "description": "A super cool tag"
 }' \
  "https://<CONSOLE>/api/v<VERSION>/tags/my_tag"
```
