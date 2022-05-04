Discovers and detects the impacted resources for the HTTP traffic in an existing WAAS out of band custom rule.

This endpoint maps to **Defend > WAAS > Out of band** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/firewall/app/out-of-band/impacted'
```

A successful response returns a list of impacted resources in the policy.