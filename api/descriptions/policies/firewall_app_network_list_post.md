Creates a new WAAS network list.

This endpoint is typically called to programmatically create a list, based on new threat intelligence.

To invoke this endpoint in the Console UI:

1. Navigate to the **Defend > WAAS > Network lists** page.
2. Click **+ Add new network list**.
3. Enter the details for the new network list and click **Save Network List**

### cURL Request

Refer to the following example cURL command that adds a new network list.

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/network-list' \
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "_id":"{id}",
   "subnets":[
      "192.145.2.3",
      "192.167.2.2"
   ]
}'
```

​**Note:** No response will be returned upon successful execution.
