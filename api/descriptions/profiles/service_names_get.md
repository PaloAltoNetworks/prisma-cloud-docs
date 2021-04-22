Retrieves the name of all host service runtime models from within the app at **Monitor > Runtime > Host-models**.

The following example curl command uses basic auth to retrieve this data:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/profiles/service/names
```
