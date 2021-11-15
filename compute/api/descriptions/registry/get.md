Retrieves registry image scan reports.

This endpoint maps to the image table in **Monitor > Compliance > Images > Registries** in the Console UI.

**Note:** In the Console UI, the images can be found in **Monitor > Vulnerabilities > Images > Registries**.

### cURL Request

The following cURL command retrieves a compact scan report for all images in the registry:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/registry"
```

The compact query can be used to get a general overview of the number of Vulnerabilities and Compliance issue counts rather than listing all the CVEs and compliance violations.

The following cURL command retrieves a compact scan report for the Ubuntu image in the registry.
The name query is synonymous with the filter registry text field in the Console UI.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/registry?name=https://<REPO-URL>/ubuntu:latest&compact=true"
```

The following cURL retrieves the scan report for the image in the registry with the matching **sha256** hash:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/registry?imageID=sha256:d461f1845c43105d7d686a9cfca9d73b0272b1dcd0381bf105276c978cb02832"
```

The following cURL command retrieves the images in the first 10 registries.
The results are returned in alphabetical order.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/registry?limit=10&offset=0&reverse=false"
```

A successful response returns the registry scan reports.
