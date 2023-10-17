Returns the Cloud Native Network Segmentation (CNNS) host audit events data in CSV format. 

For hosts, rules are defined between:
* Host to host.
* Host to an external network not protected by Prisma Cloud.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <cnns_host_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/network/host/download"
```

