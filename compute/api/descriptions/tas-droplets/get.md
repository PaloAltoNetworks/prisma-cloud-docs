Retrieves scan reports for Tanzu Application Service (TAS) droplets.

This endpoint maps to the table in **Monitor > Vulnerabilities > VMware Tanzu blobstore** in the Console UI.

### cURL Request

The following cURL command retrieves all TAS droplets.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/tas-droplets \
```

A successful response returns all TAS droplets.
