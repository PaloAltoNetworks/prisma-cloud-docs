Retrieves image scan reports.

This endpoint maps to the image table in **Monitor > Compliance > Images > Deployed** in the Console UI.

### cURL Request

The following cURL command retrieves a compact scan report for all images:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/images"
```

The following cURL command retrieves a compact scan report for an Ubuntu image.
The name query is synonymous with the filter images text field in the Console UI.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/images?name=https://<REPO-URL>/ubuntu:latest&compact=true"
```

The following cURL command retrieves the scan report for an image with the matching SHA-256 hash:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/images?id=sha256:d461f1845c43105d7d686a9cfca9d73b0272b1dcd0381bf105276c978cb02832"
```

A successful response returns the image scan reports.
