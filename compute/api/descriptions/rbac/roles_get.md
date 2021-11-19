This endpoint will return a list in JSON format of the roles can be found under Manage > Authentication > Roles

The following example curl command uses basic auth to return:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/rbac/roles
```
