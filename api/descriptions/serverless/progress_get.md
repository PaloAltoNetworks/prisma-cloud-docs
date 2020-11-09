The following curl command uses basic auth to retrieve the last Serverless scan details:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/serverless/progress
```
