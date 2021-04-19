Creates or updates a custom runtime rule.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > Runtime > Custom rules**.
2. Click **+ Add rule** or the dotted icon under the **Actions** column and choose to the **Manage** cog icon to open the update window.
3. Configure the custom rule's parameters. 
4. Click the **Add** or **Update** button to save the changes.

### cURL Request

The following cURL command updates a collection.

```bash
$ curl 'https://<CONSOLE>/api/v1/collections/<COLLECTION NAME>' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "_id":{id},
   "type":"processes",
   "message":"unexpected %proc.name was spawned",
   "name":"<CUSTOM_RULE_NAME>",
   "script":"proc.interactive"
}'
```

**Note:** No response will be returned upon successful execution.
