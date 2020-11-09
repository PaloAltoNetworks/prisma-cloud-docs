Gets details about the installed license.

The following example curl command uses basic auth to retrieve your license details.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/license
```
