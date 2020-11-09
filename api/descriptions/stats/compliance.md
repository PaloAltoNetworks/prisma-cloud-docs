Returns statistics on the number of compliance issues found on hosts/images/serverless/containers in your environment, organized by day (`_id`). This will also return a list of all of the compliance issues affecting the resources in your environment for each day.

For the current day, the response will also include detailed compliance stats for each running container and host at the time of the last scan.

The following example command that uses curl and basic auth to retrieve compliance statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/compliance
```
