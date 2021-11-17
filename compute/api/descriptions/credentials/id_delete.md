Deletes a credential from the credential store.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Credentials Store**.
2. From the table, find the row of the credential you want to delete and click the dotted icon under the **Actions** column.
3. Click the **Delete** button to open the delete confirmation window.
4. Click the **Delete Credential** button to delete the credential.

### cURL Request

The following cURL command deletes an existing credential:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/credentials/{id}
```

**Note:** No response will be returned upon successful execution.
