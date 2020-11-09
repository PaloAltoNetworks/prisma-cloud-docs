Returns all container filters in JSON format. These filters can be used in the base `GET` request as query parameters. 

A call to this api endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/containers/filters
```
