Retrieves the compliance policy for serverless functions situated in your cloud provider's infrastructure.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Compliance > Functions > Functions** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/compliance/serverless'
```

A successful response returns a list of compliance rules in the policy.
