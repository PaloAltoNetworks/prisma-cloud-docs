Returns a list of all cloud discovery scan results in a paginated response.

The parameteres under `entities` from `https://pan.dev/compute/api/22-12/get-cloud-discovery/` is now part of the response schema of a  new API endpoint `/api/v1/cloud/discovery/entities`.

### cURL Request

Refer to the following cURL example request:


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/cloud/discovery"
```
