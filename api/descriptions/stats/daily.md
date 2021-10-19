Returns daily statistics about the resources protected by Prisma Cloud Compute, including the total number of generated runtime audits, number of image vulnerabilities and compliance violations, etc.

The following example command that uses curl and basic auth to retrieve daily stats:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/daily
```
