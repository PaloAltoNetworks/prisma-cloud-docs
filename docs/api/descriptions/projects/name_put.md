Updates a project.

The following example curl command updates a project named `<PROJECT_NAME>`.
The value for `<PROJECT_NAME>` can be retrieved from the `_id` field in the response object from `GET /api/v1/projects`.

```bash
$ curl -k \
  -u <USER> \
  -X PUT \
  https://<CONSOLE>:8083/api/v1/projects/<PROJECT_NAME>
```
