Returns a summary count of compliance issues for the images, containers, hosts, and serverless functions in your environment, organized by day (`_id`).

The response also includes a detailed list of compliance issues for each running container and host at the time of the last scan.

The following example command that uses curl and basic auth to retrieve compliance statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/compliance
```
