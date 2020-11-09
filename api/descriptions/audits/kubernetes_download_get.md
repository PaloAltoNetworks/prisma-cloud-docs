Twistlock can provide events from kubernetes if this integration is configured.

The following example uses basic auth to download all kubernetes events that are configured.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o kubernetes-events.csv \
  https://console:8083/api/v1/audits/kubernetes/download
```

