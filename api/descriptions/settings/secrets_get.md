This endpoint will return configured secret store already configured in the console. This can be found in the console under **Manage > Authentication > Secrets**.

The following example curl command retrieves any configured secret stores, as well as the refresh period in hours:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/secrets
```
