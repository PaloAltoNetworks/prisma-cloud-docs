Returns a list of discovered cloud entities.

Use this API endpoint along with the `GET, api/vVERSION/cloud/discovery` to get full information about the discovered cloud scan result.

### cURL Request

Refer to the following cURL example request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/cloud/discovery/entities"
```