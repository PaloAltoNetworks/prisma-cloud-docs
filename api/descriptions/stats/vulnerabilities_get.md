Returns a summary count of CVEs in the images, containers, hosts, and serverless functions your environment, organized by day (`_id`).

The response also includes detailed descriptions for each CVE currently affecting the resources in your environment at the time of the last scan.

The following example command that uses curl and basic auth to retrieve vulnerability statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/vulnerabilities
```
