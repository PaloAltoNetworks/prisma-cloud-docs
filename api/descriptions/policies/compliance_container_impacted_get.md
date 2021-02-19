Lists the containers caught by your compliance policy on a per-rule basis.
These rule names can be found from the `name` variable in the response from a `GET` on the basic policies/compliance endpoint.

To see where Console invokes this endpoint:

* In Console, go to **Defend > Compliance > Containers and images > Deployed**.
* In the **Compliance rules** section, click **Show** under the **Entities in scope** column for a rule.
* The endpoint is invoked when the pop-up is displayed.

### cURL Request

The following cURL command returns a list of containers captured by `<RULE_NAME>`.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  'https://<CONSOLE>/api/v1/policies/compliance/container/impacted?ruleName=<RULE_NAME>'
```

A successful response contains a list of impacted containers by a rule within the context of the policy.
