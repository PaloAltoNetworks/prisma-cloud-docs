Retrieves all image scan reports.

[//]: # (https://github.com/twistlock/twistlock/issues/16586)

Note that the `discovered` field for each compliance finding (`info > allCompliance > compliance > discovered`) doesn't contain valid data and will be removed in a future release.

The following example curl command uses basic auth to retrieve the compact scan report for all images:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/images"
```

The following example curl command uses basic auth to retrieve the compact scan report for the ubuntu image.
The name query is synonymous with the "Search Images" field in the Console UI.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/images?name=https://<REPO-URL>/uqbuntu:latest&compact=true"
```

The following example curl command uses basic auth to retrieve the scan report for image with the matching sha256 hash:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/images?id=sha256:d461f1845c43105d7d686a9cfca9d73b0272b1dcd0381bf105276c978cb02832"
```
