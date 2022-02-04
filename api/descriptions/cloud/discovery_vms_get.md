Returns the discovered cloud VM instances.

### cURL Request

Refer to the following example cURL command that retrieves all the discovered cloud VM instances:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/cloud/discovery/vms'
```