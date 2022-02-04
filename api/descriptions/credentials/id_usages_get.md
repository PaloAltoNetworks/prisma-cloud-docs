Retrieves all usages for a specific credential in the credential store. 

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Credential Store**.
2. From the table, find the row of the credential you want to update and click the dotted icon under the **Actions** column.
3. Click the **Manage** button.
4. The **Usage** table displays the data from this endpoint.

### cURL Request

Refer to the following cURL command that retrieves all usages for a credential:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/credentials/{id}/usages
```

A successful response returns a list of all usages for the credential.
