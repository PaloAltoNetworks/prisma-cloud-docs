Returns statistics about the resources protected by Prisma Cloud Compute, including the total number of runtime audits, image vulnerabilities, and compliance violations.

The following example command that uses curl and basic auth to retrieve dashboard stats:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/dashboard
```
