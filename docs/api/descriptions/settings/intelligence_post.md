Configures the Intelligence Stream.

For more information, see [Intelligence Stream](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/technology_overviews/intel_stream)

### cURL Request

Refer to the following example cURL command that uses basic auth to configure settings of your Intelligence Stream.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d ' {
   "windowsFeedEnabled": true,
   "enabled": true,
   "address": "https://intelligence.example.com",
   "token": "<TOKEN>",   
}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/intelligence"
```
