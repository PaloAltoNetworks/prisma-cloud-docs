Adds a new user to the system.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"username":"<USERNAME>","password":",<PASSWORD>","role":"user","authType":"basic","projects":[],"collections":["All"]}' \
  https://<CONSOLE>:8083/api/v1/users
```
