Refreshes the current day's CVE counts and CVE list, as well as their descriptions.

This endpoint returns the same response as `/api/v<VERSION>/stats/vulnerabilities`, but with updated data for the current day.

### cURL Request

Refer to the following example cURL command that refreshes the vulnerability statistics for current day:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  'https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/refresh'
```
A successful response returns a summary count of the CVEs and detailed descriptions for each CVE for the current day.
