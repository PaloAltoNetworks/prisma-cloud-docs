Retrieves the compliance policy for hosts protected by Defender.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Compliance > Hosts > Running hosts** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/compliance/host'
```

A successful response returns a list of compliance rules in the policy.
