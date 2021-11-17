Prisma Cloud Compute can provide events from Kubernetes if this integration is configured.

The following example downloads all Kubernetes events that are configured.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o kubernetes-events.csv \
  https://console:8083/api/v1/audits/kubernetes/download
```

