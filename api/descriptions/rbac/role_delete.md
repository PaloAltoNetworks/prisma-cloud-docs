This endpoint will delete a specific role by its name from page **Manage > Authentication > Roles**
System roles and roles assigned to users/groups cannot be deleted.

The following example curl command uses basic auth to delete role:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/roles/<ROLENAME>
```
