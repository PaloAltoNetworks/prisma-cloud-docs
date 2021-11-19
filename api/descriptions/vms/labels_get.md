Returns an array of strings containing all AWS tags of the scanned VM images.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/vms/labels
```
