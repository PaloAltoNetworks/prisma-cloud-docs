This endpoint will return all system settings in JSON format.

The following example curl command does exactly that:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/system
```
