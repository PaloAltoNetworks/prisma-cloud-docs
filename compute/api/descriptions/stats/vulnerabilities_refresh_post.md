Refreshes the current day's CVE counts and CVE list, as well as their descriptions.

This endpoint returns the same response as `/api/v1/stats/vulnerabilities`, but with updated data for the current day.

The following example command that uses curl and basic auth to refresh the vulnerability statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/stats/vulnerabilities/refresh
```
