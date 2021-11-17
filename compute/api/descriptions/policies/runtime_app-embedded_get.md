Retrieves the runtime policy for apps protected by App-Embedded Defenders.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Runtime > App-Embedded policy** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/runtime/app-embedded'
```

A successful response returns a list of runtime rules in the policy.
