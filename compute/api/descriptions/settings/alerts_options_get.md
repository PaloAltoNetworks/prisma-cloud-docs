This endpoint will return the alert profile configuration options that can be found in the console under the alert type selection when setting up a new alert profile.

The following example curl command uses basic auth to retrieve all alert profile configuration options:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/alerts/options
```
