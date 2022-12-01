Returns the Cloud Native Network Segmentation (CNNS) container audit events data in CSV format. 

For more information, see the [Cloud Native Network Segmentation (CNNS)](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/firewalls/cnns_saas) 

For containers, rules are defined between:
* Image to image.
* Image to Image to an external network not protected by Prisma Cloud.
* Image to DNS domain.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o <cnns_container_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/network/container/download"
```
