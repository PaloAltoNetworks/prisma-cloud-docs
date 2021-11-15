Returns a list of the Linux kernel system calls.
Runtime rules for containers can allow-list and deny-list specific system calls.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/static/syscalls
```
