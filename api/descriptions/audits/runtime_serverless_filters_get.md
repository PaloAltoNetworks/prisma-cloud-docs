Returns all serverless filters in JSON format. These filters can be used in the base `GET` request as query parameters. 

A call to this api endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://CONSOLE_ADDRESS:PORT/api/v1/audits/runtime/serverless/filters
```

