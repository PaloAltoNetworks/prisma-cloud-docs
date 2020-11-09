Retrieves all host scan reports. A curl command to access this endpoint may resemble the following code snippet.

[//]: # (https://github.com/twistlock/twistlock/issues/16586)

Note that the `discovered` field for each compliance finding (`info > allCompliance > compliance > discovered`) doesn't contain valid data and will be removed in a future release.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/hosts \
```
