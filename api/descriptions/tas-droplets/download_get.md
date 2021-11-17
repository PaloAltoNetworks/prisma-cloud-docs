Downloads scan reports for Tanzu Application Service (TAS) droplets in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > VMware Tanzu blobstore** in the Console UI.

### cURL Request

The following cURL command downloads all TAS droplets to a CSV file called `tas_droplets.csv`:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/tas-droplets/download \
  > tas_droplets.csv
```

A successful response displays the status of the download.
