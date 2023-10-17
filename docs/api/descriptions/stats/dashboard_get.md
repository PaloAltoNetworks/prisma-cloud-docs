Returns statistics about the resources protected by Prisma Cloud Compute, including the total number of runtime audits, image vulnerabilities, and compliance violations.

### cURL Request

Refer to the following example cURL command that retrieves dashboard stats:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/stats/dashboard
```
