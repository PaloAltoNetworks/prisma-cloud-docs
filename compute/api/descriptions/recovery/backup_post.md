Creates a backup named `backup_name` by invoking the MongoDB dump process.

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d "{backup_name}" \
  https://<CONSOLE>:8083/api/v1/recovery/backup
```
