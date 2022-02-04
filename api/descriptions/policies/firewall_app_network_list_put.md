Updates an existing WAAS network list.

This endpoint is typically called to programmatically update a network list, based on new threat intelligence.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > WAAS > Network lists** page.
2. Click on an existing list in the table and update the list as required.
3. Click **Update Network List** to save the changes.

### cURL Request

Refer to the following example cURL command that updates a network list.

```bash
$ curl 'https://<CONSOLE>/api/v1/policies/firewall/app/network-list' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "_id":"{id}",
   "subnets":[
      "192.145.3.3",
      "192.167.3.2"
   ]
}'
```

​**Note:** No response will be returned upon successful execution.
