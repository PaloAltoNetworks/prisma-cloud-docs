Retrieves the list of Jenkins projects that have been scanned by the Jenkins plugin. Each project in the `jobName` array can be used to query the base `api/v1/scans` endpoint to retrieve only scan reports in that Jenkins project.

The following example curl command uses basic auth to retrieve the list of Jenkins project names:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/scans/filters
```
