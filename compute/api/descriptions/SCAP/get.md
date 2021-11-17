This endpoint will return any SCAP datastreams uploaded to the console. This endpoint will return a 404 error if you have not configured your console to consume SCAP datastreams.

The following is an example curl command that uses basic auth to retrieve any uploaded datastreams configured for SCAP scanning:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/scap
```
