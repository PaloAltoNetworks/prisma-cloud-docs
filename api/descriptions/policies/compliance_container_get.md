Retrieves the compliance policy for running containers.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Compliance > Containers and images > Deployed** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/compliance/container'
```

A successful response returns a list of compliance rules in the policy.
