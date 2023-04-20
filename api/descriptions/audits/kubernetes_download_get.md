Returns the audit events data that occur in an integrated Kubernetes cluster that you configured for Prisma Cloud Compute under **Defend > Access > Kubernetes** in CSV format.

**Note:** This endpoint relates to the **Monitor > Events > Kubernetes** audits in Prisma Cloud Compute.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <kubernetes_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/kubernetes/download"
```

