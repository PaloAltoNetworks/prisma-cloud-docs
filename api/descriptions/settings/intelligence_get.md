Gets details about the Intelligence Stream configuration.

The following example curl command uses basic auth to retrieve your Intelligence Stream configuration settings.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/intelligence
```
