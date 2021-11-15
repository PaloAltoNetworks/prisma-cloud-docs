Retrieves the details and state of all runtime models.

The following example command uses curl and basic auth to install a list of all runtime models in the system:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/profiles/container
```
