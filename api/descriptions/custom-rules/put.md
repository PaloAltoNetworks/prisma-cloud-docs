Creates or updates a custom rule.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > Custom rules**.
2. Click **+ Add rule** or the dotted icon under the **Actions** column and choose to the **Manage** cog icon to open the update window.
3. Configure the custom rule's parameters. 
4. Click the **Add** or **Update** button to save the changes.

### cURL Request

Refer to the following example cURL command that updates a custom rule.

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/custom-rules/{id}' \
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
