Retrieves all scan reports for the serverless functions that Twistlock has been configured to scan.

[//]: # (https://github.com/twistlock/twistlock/issues/16586)

Note that the `discovered` field for each compliance finding (`info > allCompliance > compliance > discovered`) doesn't contain valid data and will be removed in a future release.

The following example curl command uses basic auth to retrieve the scan reports for your serverless functions:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/serverless
```
