Retrieves registry image scan reports.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds.
You get an HTTP error response 429 if the limit exceeds.

This endpoint maps to **Monitor > Compliance > Images > Registries** in the Console UI.

> _**Note:**_ In the Console UI, the images can be found in **Monitor > Vulnerabilities > Images > Registries**.

Consider the following available options to retrieve when you use the `fields` query parameter:
- labels
- repoTag.repo
- repoTag.registry
- clusters
- hosts
- repoTag.tag

### cURL Request

Refer to the following cURL command that retrieves a scan report for all images in the registry:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry"
```

The compact query can be used to get a general overview of the number of Vulnerabilities and Compliance issue counts rather than listing all the CVEs and compliance violations.

Refer to the following cURL command that retrieves a compact scan report for the Ubuntu image in the registry:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry?name=https://<REPO-URL>/ubuntu:latest&compact=true"
```
The name query is synonymous with the filter registry text field in the Console UI.

Refer to the following cURL that retrieves the scan report for the image in the registry with the matching **sha256** hash:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry?imageID=sha256:d461f1845c43105d7d686a9cfca9d73b0272b1dcd0381bf105276c978cb02832"
```

Refer to the following cURL command that retrieves the images in the first 10 registries:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry?limit=10&offset=0&reverse=false"
```

A successful response returns the registry scan reports in alphabetical order.
