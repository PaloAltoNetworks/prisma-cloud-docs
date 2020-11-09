Retrieves all container scan reports.

[//]: # (https://github.com/twistlock/twistlock/issues/16586)

Note that the `discovered` field for each compliance finding (`info > allCompliance > compliance > discovered`) doesn't contain valid data and will be removed in a future release.

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/containers
```
