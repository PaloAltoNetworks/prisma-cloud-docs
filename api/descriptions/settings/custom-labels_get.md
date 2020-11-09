Retrieves the list of [alert labels](https://docs.twistlock.com/docs/latest/audit/annotate_audits.html) configured in Console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/custom-label
```
