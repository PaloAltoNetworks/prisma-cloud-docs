Retrieves the compliance policy for serverless functions built in your Continuous Integration (CI) pipeline.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Compliance > Functions > CI** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/policies/compliance/ci/serverless
```

A successful response contains a list of compliance rules in the policy.

