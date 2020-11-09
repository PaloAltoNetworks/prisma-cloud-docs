Retrieves the current registry scan progress. THis will provide the current scanner running, the image currently being scanned, and the time of the scan. If no scan is running, `discovery` parameter will be set to false.

The following example curl command uses basic auth to retrieve the current registry scan progress:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/registry/progress
```
