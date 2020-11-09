Updates an existing user in the system.

The following example command changes the role of user `butterbean` to `defenderManager`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"username":"butterbean","role":"defenderManager"}' \
  https://<CONSOLE>:8083/api/v1/users
```
