Deletes a collection.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Collections and Tags > Collections**.
2. Click the dotted icon under the **Actions** column to open up the menu options. **Note:** The default collections do not have a dotted icon in the **Actions** column.
3. Click the **Delete** button to initiate the deletion. 
4. Click the **Delete Collection** button to confirm the deletion.

### cURL Request

Refer to the following example cURL command that deletes a collection with the name `my-collection`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  'https://<CONSOLE>/api/v<VERSION>/collections/my-collection'
```

**Note:** No response will be returned upon successful execution.
