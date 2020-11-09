This endpoint will trigger a Kubernetes scan.

The following example curl command uses basic auth to initiate this scan:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/kubernetes/scan
```
