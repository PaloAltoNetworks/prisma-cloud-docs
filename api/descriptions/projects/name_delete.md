Deletes a project from the system.

The following example curl command deletes a project named `<PROJECT_NAME>`.
The value for `<PROJECT_NAME>` can be retrieved from the `_id` field in the response object from `GET /api/v1/projects`.

The DELETE method returns the decommissioned supervisor's admin username and password.

```bash
$ curl -k \
  -u <USER> \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/projects/<PROJECT_NAME>
```
