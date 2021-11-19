Deletes an existing Defender on a given host.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Defenders > Defenders**.
2. In a table row, click the dotted **Actions** button for the Defender you want to delete.
3. Click the **Decommission** button to open the delete confirmation window.
4. Click the **Delete Defender** button to delete the Defender.

### cURL Request

The following cURL command deletes an existing Defender on a host.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>/api/v1/defenders/<HOSTNAME>
```

`<HOSTNAME>` is populated with a value returned from the `/api/v1/defenders/names` endpoint.

**Note:** No response will be returned upon successful execution.
