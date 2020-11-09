Returns an array of strings containing VM image names.

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H 'Content-Type: application/json' \
  https://<CONSOLE>:8083/api/v1/vms/names
```
