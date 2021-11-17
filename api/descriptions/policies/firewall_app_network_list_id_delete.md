Deletes an existing WAAS network list.

This endpoint is typically called to programmatically delete a network list, based on new threat intelligence.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > WAAS > Network lists** page.
2. Locate an existing list in the table to delete and click the trash icon under the **Actions** columns.
3. Click **Delete Network List** to confirm the deletion.

### cURL Request

The following cURL command adds a new network list.

```bash
$ curl 'https://<CONSOLE>/api/v1/policies/firewall/app/network-list/{id}' \
  -k \
  -X DELETE \
  -u <USER>
```

​**Note:** No response will be returned upon successful execution.
