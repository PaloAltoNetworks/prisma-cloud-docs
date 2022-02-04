Retrieves the runtime policy for apps protected by App-Embedded Defenders.
A policy consists of ordered rules.

This endpoint maps to **Defend > Runtime > App-Embedded policy** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/runtime/app-embedded'
```

A successful response returns a list of runtime rules in the policy.
