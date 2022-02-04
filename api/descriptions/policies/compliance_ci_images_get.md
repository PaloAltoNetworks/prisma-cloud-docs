Retrieves the compliance policy for images scanned in your continuous integration (CI) pipeline.
A policy consists of ordered rules.

This endpoint maps to **Defend > Compliance > Containers and images > CI** in the Console UI.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/policies/compliance/ci/images'
```

A successful response returns a list of compliance rules in the policy.
