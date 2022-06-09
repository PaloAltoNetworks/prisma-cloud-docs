Deletes a credential from the credential store.

**Note:** Use only Prisma Cloud Compute user interface **Manage** > **Cloud accounts** to delete cloud credentials for `Amazon AWS`, `Microsoft Azure`, and `Google Cloud Platform`. 

To invoke this endpoint in the Prisma Cloud Compute user interface:

1. Navigate to **Manage > Authentication > Credentials Store**.
2. From the table, find the row of the credential you want to delete and click the dotted icon under the **Actions** column.
3. Click the **Delete** button to open the delete confirmation window.
4. Click the **Delete Credential** button to delete the credential. 

### cURL Request

Refer to the following example cURL command that deletes an existing credential:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>/api/v<VERSION>/credentials/{id}
```

**Note:** No response will be returned upon successful execution.
