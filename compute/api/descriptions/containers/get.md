Retrieves container scan reports.

This endpoint maps to the image table in **Monitor > Compliance > Images > Deployed** in the Console UI.

### cURL Request

The following cURL command retrieves a scan report for all containers:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/containers"
```

The following cURL command retrieves a scan report for an container with the collection `<COLLECTION ID>`.
The name query is synonymous with the filter containers text field in the Console UI.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/containers?collections=<COLLECTION ID>"
```

A successful response returns the container scan reports.
