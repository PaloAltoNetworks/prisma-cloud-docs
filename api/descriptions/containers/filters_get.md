Returns all container filters in JSON format. These filters can be used in the base `GET` request as query parameters. 

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/containers/filters
```
