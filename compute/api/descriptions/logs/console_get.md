Retrieves the latest Console log messages.

The following example curl command retrieves the 10 latest Console log messages:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/logs/console?lines=10
```
