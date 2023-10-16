Retrieves a list of all WAAS policy rules for serverless functions.

This endpoint maps to **Defend > WAAS > Serverless** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/serverless'
```

A successful response returns a list of firewall rules in the policy.
