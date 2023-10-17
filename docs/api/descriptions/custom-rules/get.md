Retrieves a list of all custom rules.

This endpoint maps to the policy table in **Defend > Custom rules** in the Console UI.

### cURL Request

Refer to the following example cURL command that retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/custom-rules'
```

A successful response returns a list of custom rules in the policy.
