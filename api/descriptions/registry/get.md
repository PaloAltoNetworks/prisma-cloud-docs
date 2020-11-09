Retrieves all scan reports for registry images that Twistlock has been configured to scan.
In the Console UI, these are images that can be found in **Monitor > Vulnerabilities > Images > Registries**.

[//]: # (https://github.com/twistlock/twistlock/issues/16586)

Note that the `discovered` field for each compliance finding (`info > allCompliance > compliance > discovered`) doesn't contain valid data and will be removed in a future release.

The following example curl command uses basic auth to retrieve the scan report for all images in the registry:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/registry"
```

The compact query can also be used to get a general overview of the number of Vulnerabilities and Compliance issue counts instead of listing all of CVEs and compliance violations.
The following example curl command uses basic auth to retrieve the compact scan report for the ubuntu image in the registry.  The name query is synonymous with the **Search Registry** field in the Console UI:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/registry?name=https://<REPO-URL>/uqbuntu:latest&compact=true"
```

The following example curl command uses basic auth to retrieve the scan report for the image in the registry with the matching **sha256** hash:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/registry?imageID=sha256:d461f1845c43105d7d686a9cfca9d73b0272b1dcd0381bf105276c978cb02832"
```

The following example curl command uses basic auth to retrieve the scan reports in pages, in a similar way to the Console UI.
This example returns the first ten scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/registry?limit=10&offset=0"
```

The following example curl command uses basic auth to retrieve the scan reports in pages, in a similar way to the UI.
This example returns the results in alphabetical order.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/registry?limit=10&offset=0&reverse=false"
```
