This endpoint will delete any SCAP datastreams uploaded to the console. You can find `xml_name` from the `GET /api/v1/scap` endpoint.

The following is an example curl command that uses basic auth to delete an uploaded datastreams configured for SCAP scanning:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/scap/{xml_name}
```
