Retrieves container scan reports.

This endpoint maps to **Monitor > Compliance > Images > Deployed** in the Console UI.

Refer to the following available options for the `fields` query parameters:
* labels
* externalLabels
* cluster
* hostname
* image

### cURL Request

Refer to the following example cURL command that retrieves a scan report for all containers:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/containers"
```

Refer to the following example cURL command that retrieves a scan report for a container with the collection `<COLLECTION ID>`:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/containers?collections=<COLLECTION ID>"
```
The name query is synonymous with the filter containers text field in the Console UI.

A successful response returns the container scan reports.
