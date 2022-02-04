Returns an integer representing the number of containers in your environment.

### cURL Request

Refer to the following example cURL command that returns the number of containers.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/containers/count
```
