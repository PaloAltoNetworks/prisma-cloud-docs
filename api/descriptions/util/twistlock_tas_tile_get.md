Downloads the VMware Tanzu Application Service tile for Prisma Cloud Compute.

Although this endpoint is supported, no backwards compatibility is offered for it.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -L \
  -o twistlock-tile.pivotal \
  "https://<CONSOLE>/api/v1/util/tas-tile"
```

A successful response displays the status of the download.