Prisma Cloud Compute can provide events from Kubernetes if this integration is configured.

The following example lists all Kubernetes events that are configured.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/kubernetes
```

