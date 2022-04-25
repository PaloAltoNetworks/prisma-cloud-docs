Retrieves the compliance policy for running containers.
A policy consists of ordered rules.

This endpoint maps to **Defend > Compliance > Containers and images > Deployed** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/compliance/container'
```

A successful response returns a list of compliance rules in the policy.
