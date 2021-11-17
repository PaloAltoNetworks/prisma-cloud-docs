Updates a credential in the credentials store.

To invoke this endpoint in the Console UI:

1. Navigate to **Manage > Authentication > Credentials Store**.
2. From the table, find the row of the credential you want to update and click the dotted icon under the **Actions** column.
3. Click the **Manage** button and update the credential's parameters.
4. Click the **Save** button to save the updated credential.

### cURL Request

The following cURL command updates a credential:

```bash
$ curl 'https://<CONSOLE>/api/v1/users' \
  -k \
  -X PUT \
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

**Note:** No response will be returned upon successful execution.

