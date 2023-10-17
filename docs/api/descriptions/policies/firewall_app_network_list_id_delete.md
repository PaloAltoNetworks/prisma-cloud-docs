Deletes an existing WAAS network list.

This endpoint is typically called to programmatically delete a network list, based on new threat intelligence.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > WAAS > Network lists** page.
2. Locate an existing list in the table to delete and click the trash icon under the **Actions** columns.
3. Click **Delete Network List** to confirm the deletion.

### cURL Request

Refer to the following example cURL command that deletes a new network list.

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/network-list/{id}' \
  -k \
  -X DELETE \
  -u <USER> \
  -H 'Content-Type: application/json'
```

​**Note:** No response will be returned upon successful execution.
