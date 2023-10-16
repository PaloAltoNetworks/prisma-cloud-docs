Retrieves the details and state of all runtime models in CSV format.


## cURL Request

Refer to the following example cURL command that downloads a complete list in CSV format:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o <FILE NAME> \
  https://<CONSOLE>/api/v<VERSION>/profiles/container/download
```
