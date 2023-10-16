Returns the docker access audit events data in CSV format that are logged and aggregated for any container resource protected by a Defender in Prisma Cloud Compute.

**Note**: You can download the access events from Console under **Monitor > Events > Docker audits > Download CSV**.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -O <access_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/access/download?type=docker"
```
