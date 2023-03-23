Retrieves the compliance policy for VM images scanned in your cloud accounts.
A policy consists of ordered rules.

This endpoint maps to the policy table in **Defend > Compliance > Hosts > VM images** in the Console UI.

### cURL Request

The following cURL command retrieves all rules in the policy.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/compliance/vms'
```

A successful response returns a list of compliance rules in the policy.