Gets the Cloud Controller Addresses of scanned Tanzu Application Service (TAS) droplets.\n 

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds. 
You get an HTTP error response 429 if the limit exceeds.


### cURL Request

The following cURL command retrieves the Cloud Controller Addresses of scanned TAS droplets.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/tas-droplets/addresses \
```