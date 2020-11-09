Lists all projects visible to the given user.

Assuming the given user is an admin, the following example curl command would list all projects:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/projects
```
