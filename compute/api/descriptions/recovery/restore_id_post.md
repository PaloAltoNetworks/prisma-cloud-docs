Restores Prisma Cloud Compute from the given backup.

`{file_name_of_backup} = {backup_name}-18.11.128-1551386737.tar.gz`

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/recovery/restore/{file_name_of_backup}
```
