Retrieves container scan reports.

You can view the container scan reports in Console under **Monitor > Compliance > Containers**.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds.
You get an HTTP error response 429 if the limit exceeds.

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
