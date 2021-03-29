Deletes a group from the system.
The `id` can be retrieved from the `GET /api/v1/groups` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/groups
```
