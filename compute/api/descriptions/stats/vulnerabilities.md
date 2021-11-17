Returns statistics on the number of CVEs found on hosts/images/serverless/containers in your environment, organized by day (`_id`). This will also return a list of all of the CVEs affecting the resources in your environment for each day.

For the current day, the response will also include descriptions of the CVEs currently affecting the resources in your environment.

The following example command that uses curl and basic auth to retrieve vulnerability statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/vulnerabilities
```
