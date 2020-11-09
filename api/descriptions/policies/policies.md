Manage your rules and policies programatically.

Policies are sets of ordered rules.
[Rule order](https://docs.twistlock.com/docs/latest/configure/rule_ordering_pattern_matching.html) determines how a policy is evaluated.

In general, the policy endpoints don't have DELETE methods.
Use the PUT method to delete all rules by submitting an empty JSON object.
For example, to delete all host runtime rules:

```
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{}' \
  https://<CONSOLE>:8083/api/v1/policies/runtime/host
```
