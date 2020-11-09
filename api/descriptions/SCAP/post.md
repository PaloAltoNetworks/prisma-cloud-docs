This endpoint will allow you to add a SCAP datastream to the console.

The following is an example curl command that uses basic auth to add an uploaded datastreams configured for SCAP scanning:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"XMLName":{"Space":"","Local":""}}' \
  https://<CONSOLE>:8083/api/v1/scap
```
