Deletes all host audits from the database.

The following example curl command uses basic auth to delete all host audits:

```bash
$ curl -k \
  -u <USER> \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/audits/runtime/host
```
