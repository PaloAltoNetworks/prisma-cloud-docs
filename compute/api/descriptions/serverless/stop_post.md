If there is an ongoing serverless scan that is running, this curl command will use basic auth to stop the current serverless scan:

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/serverless/stop
```
