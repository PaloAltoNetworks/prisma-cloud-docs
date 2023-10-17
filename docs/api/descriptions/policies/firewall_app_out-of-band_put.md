Updates or edits a WAAS custom rule for out of band traffic.
A policy consists of ordered rules.

This endpoint maps to **Defend > WAAS > Out of band** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/out-of-band' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'{
   "rules":[
      {
         "name":"my-rule",
         "effect":"disable",
         "collections":[
            {
               "name":"All"
            }
         ],
      }
   ],
}'
```