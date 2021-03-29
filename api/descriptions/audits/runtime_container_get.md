Twistlock records an audit every time a runtime sensor (process, network, file system, and system call) detects activity that deviates from the predictive model.
This endpoint retrieves all container audits from the console **Monitor > Runtime > Container Audits**.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/runtime/container
```
