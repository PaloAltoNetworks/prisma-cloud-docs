Discovers and detects the HTTP traffic for an existing WAAS out of band custom rule.
A policy consists of ordered rules.

This endpoint maps to **Defend > WAAS > Out of band** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/out-of-band'
```

A successful response returns a list of rules in the policy.