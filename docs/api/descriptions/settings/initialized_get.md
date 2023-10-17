Checks whether Console has been configured with an initial admin account.
After first installing Console, the first thing you must do is create an admin account.

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/initialized
```
