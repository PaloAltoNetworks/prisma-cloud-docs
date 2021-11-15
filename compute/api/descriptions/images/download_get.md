Downloads image scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Compliance > Images > Deployed** in the Console UI.

### cURL Request

The following cURL command generates a CSV file containing the scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/images/download?id={id}&layers=true" \
  > images.csv
```

The following cURL command is particularly useful for developers.
It takes an image ID as the input parameter, and generates a CSV file that lists all vulnerable packages in a given image, organized by layer, with both the affected and fixed versions.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/images/download?id={id}&layers=true" \
  > images.csv
```

Where an example `{id}` would be `sha256:abd4f451ddb707c8e68a36d695456a515cdd6f9581b7a8348a380030a6fd7689`.

A successful response displays the status of the download.
