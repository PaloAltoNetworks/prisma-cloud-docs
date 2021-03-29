Retrieves the runtime policy for containers protected by Defender.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Runtime > Container policy** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/runtime/container'
```

A successful response returns a list of runtime rules in the policy.
