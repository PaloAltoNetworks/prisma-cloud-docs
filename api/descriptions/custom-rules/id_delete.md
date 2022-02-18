Deletes a custom rule.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > Custom rules** page.
2. Click the dotted icon under the **Actions** column to open the menu options.
3. Click the **Delete** button to initiate the deletion. 
4. Click the **Delete Rule** button to confirm the deletion.

### cURL Request

Refer to the following example cURL command adds a new network list.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  'https://<CONSOLE>/api/v<VERSION>/custom-rules/{id}'
```

​**Note:** No response will be returned upon successful execution.
