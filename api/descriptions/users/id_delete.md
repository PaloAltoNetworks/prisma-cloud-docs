Deletes a user from the system by username.

The following example command deletes a specific user from the system.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/users/<USERNAME>
```
