Retrieves scan reports for Tanzu Application Service (TAS) droplets.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds.
You get an HTTP error response 429 if the limit exceeds.

This endpoint maps to the table in **Monitor > Vulnerabilities > VMware Tanzu blobstore** in the Console UI.

### cURL Request

The following cURL command retrieves all TAS droplets.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/tas-droplets \
```

A successful response returns all TAS droplets.
