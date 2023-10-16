Updates a credential in the credentials store.

**Note:** Use only Prisma Cloud Compute user interface **Manage** > **Cloud accounts** > **Add account** to add cloud credentials for `Amazon AWS`, `Microsoft Azure`, and `Google Cloud Platform`.

To invoke this endpoint in the Prisma Cloud Compute user interface:

1. Navigate to **Manage > Authentication > Credentials Store**.
2. From the table, find the row of the credential you want to update and click the dotted icon under the **Actions** column.
3. Click the **Manage** button and update the credential's parameters.
4. Click the **Save** button to save the updated credential.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/credentials' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "serviceAccount":{      
   },
   "apiToken":{
      "encrypted":"ENCRYPTED_TOKEN"
   },
   "type":"TYPE",
   "_id":"{id}"
}'
```

**Note:** There's no response upon successful execution.

