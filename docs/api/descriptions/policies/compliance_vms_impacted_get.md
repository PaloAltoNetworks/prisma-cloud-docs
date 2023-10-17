Retrieves a list of all resources a compliance rule impacts.
These rule names can be found from the `name` variable in the response from a `GET` on the basic policies/compliance endpoint.

Use query parameters to retrieve the list of impacted resources by *account ID*, *rule name*, or *collection*.

### cURL Request

Refer to the following example cURL command, which retrieves a list of impacted resources:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/policies/compliance/vms/impacted"
```
