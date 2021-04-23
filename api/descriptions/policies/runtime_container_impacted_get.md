Returns the impacted images based on a given rule
In the Console UI, you can see how it works by going to the **Defend > Runtime > Container policy** page and clicking the **Show** link.

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/policies/runtime/container/impacted?ruleName={ruleName}
```

For additional help with your `ruleName`:

```bash
$ curl -k -G \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  --data-urlencode 'ruleName=Default - alert on suspicious runtime behavior' \
  https://<CONSOLE>:8083/api/v1/policies/runtime/container/impacted
```
