Twistlock can provide events from kubernetes if this integration is configured.

The following example uses basic auth to list all kubernetes events that are configured.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/kubernetes
```

