Retrieves a list of all secrets rules.

The following curl command uses basic auth to retrieve a list of all rules, pretty-print the JSON response, and save the results to a file.

```
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/policies/secrets
```
