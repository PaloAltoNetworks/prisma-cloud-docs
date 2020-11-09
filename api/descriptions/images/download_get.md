Downloads all image scan reports in CSV format.

The following command is particularly useful for developers.
It takes an image ID as the input parameter, and generates a CSV file that lists all vulnerable packages in a given image, organized by layer, with both the affected and fixed versions.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/images/download?id=<IMAGE_ID>&layers=true" \
  > images.csv
```

Where an example &lt;IMAGE_ID&gt; would be `sha256:abd4f451ddb707c8e68a36d695456a515cdd6f9581b7a8348a380030a6fd7689`.
