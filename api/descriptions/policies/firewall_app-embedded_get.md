Retrieves the WAAS policy for web apps protected by App-Embedded Defender.
A policy consists of ordered rules.

This endpoint maps to the table in **Defend > WAAS > App-Embedded** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/firewall/app/app-embedded'
```

A successful response returns a list of rules in the policy.
