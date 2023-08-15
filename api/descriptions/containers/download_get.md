Downloads container scan reports in CSV format.

You can download the container scan reports in CSV format in Console under **Monitor > Compliance > Containers**.

**Note**: The query parameter `fields` is not supported for this API endpoint.

### cURL Request

Refer to the following example cURL command that generates a CSV file containing the scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/containers/download?id={id}&layers=true" \
  > container_report.csv
```

A successful response displays the status of the download.
