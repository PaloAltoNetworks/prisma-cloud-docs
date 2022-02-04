Retrieves the runtime policy for containers protected by Defender.
A policy consists of ordered rules.

This endpoint maps to **Defend > Runtime > Container policy** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/runtime/container'
```

A successful response returns a list of runtime rules in the policy.
