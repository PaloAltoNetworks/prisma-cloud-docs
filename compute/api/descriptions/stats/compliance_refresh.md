Refreshes the current day's compliance violations counts and list, as well as the affected running resources.

The response will return exactly what the /statistics/compliance endpoint returns, only with updated statistics for the current day.

The following example command that uses curl and basic auth to refresh compliance statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/stats/compliance
```
