Returns a list of all cloud discovery scan results in a paginated response.

The `entities` object and the associated parameters in the response schema is now part of a new API endpoint `/api/v1/cloud/discovery/entities`.

### cURL Request

Refer to the following cURL example request:


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/cloud/discovery"
```
