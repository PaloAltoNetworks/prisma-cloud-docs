Deletes all container runtime audits.

The following example curl command uses basic auth to delete all the audits:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/audits/runtime/container
```
