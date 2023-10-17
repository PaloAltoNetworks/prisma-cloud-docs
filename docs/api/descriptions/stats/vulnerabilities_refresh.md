Refreshes the current day's CVE counts and CVE list, as well as their descriptions.

The response will return exactly what the /statistics/vulnerabilities endpoint returns, only with updated statistics for the current day.

The following example command that uses curl and basic auth to refresh vulnerability statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/stats/vulnerabilities/refresh
```
