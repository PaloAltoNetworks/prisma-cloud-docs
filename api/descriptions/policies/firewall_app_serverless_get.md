Retrieves a list of all WAAS policy rules for serverless functions.

This endpoint maps to the policy table in **Defend > WAAS > Serverless** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```
$ curl -k \
  -u <USER> \
  https://<CONSOLE>/api/v1/policies/firewall/app/serverless
```

A successful response returns a list of firewall rules in the policy.
