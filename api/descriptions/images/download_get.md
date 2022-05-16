Downloads image scan reports in CSV format.

This endpoint maps to **Monitor > Compliance > Images > Deployed** in the Console UI.

Consider the following available options to retrieve when you use the `fields` query parameter:
- labels
- repoTag.repo
- repoTag.registry
- clusters
- hosts
- repoTag.tag

### cURL Request

Refer to the following cURL command that generates a CSV file containing the scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/images/download" \
  > images.csv
```

Refer to the following example cURL command that might be useful for developers:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/images/download?id={id}&layers=true" \
  > images.csv
```
where an example `{id}` is `sha256:abd4f451ddb707c8e68a36d695456a515cdd6f9581b7a8348a380030a6fd7689`.

It takes an image ID as the input parameter, and generates a CSV file that lists all vulnerable packages in a given image, organized by layer, with both the affected and fixed versions.

A successful response displays the status of the download.
