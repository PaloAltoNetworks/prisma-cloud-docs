Deletes a given backup by name.

`{file_name_of_backup} = {backup_name}-18.11.128-1551386737.tar.gz`

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PATCH \
  -d '"{new_name}"'
  https://<CONSOLE>:8083/api/v1/recovery/backup/{file_name_of_backup}
```
