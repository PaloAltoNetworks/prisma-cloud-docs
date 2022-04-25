Retrieves the WAAS policy for containers.
A policy consists of ordered rules.

This endpoint maps to **Defend > WAAS > Container** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/container'
```

A successful response returns a list of rules in the policy.
