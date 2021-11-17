Retrieves a list of all custom runtime rules.

This endpoint maps to the policy table in **Defend > Runtime > Custom rules** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/runtime/custom-rules'
```

A successful response returns a list of custom rules in the policy.
