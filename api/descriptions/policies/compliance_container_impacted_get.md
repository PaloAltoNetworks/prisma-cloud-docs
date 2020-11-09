Retrieves a list of all resources a compliance rule impacts.
These rule names can be found from the `name` variable in the response from a `GET` on the basic policies/compliance endpoint.

The following example curl command uses basic auth to retrieve a list of resources that currently violate rule `compliance_rule`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/policies/compliance/container?ruleName=compliance_rule"
```
