Deletes a group.
The `id` can be retrieved from the `GET /api/v1/groups` endpoint.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Groups**.
2. Click the dotted icon under the **Actions** column to open the menu options.
3. Click the **Delete** button to initiate the deletion. 
4. Click the **Delete Group** button to confirm the deletion.

### cURL Request

The following cURL command deletes a collection with the name `{id}`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  'https://<CONSOLE>/api/v1/groups/{id}'
```

**Note:** No response will be returned upon successful execution.
