Refreshes the current day's list and counts of compliance issues, as well as the list of affected running resources.

This endpoint returns the same response as /api/v1/stats/compliance, but with updated data for the current day.

The following example command that uses curl and basic auth to refresh compliance statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/stats/compliance
```
