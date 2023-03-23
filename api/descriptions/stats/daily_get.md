Returns a historical list of per-day statistics for the resources protected by Prisma Cloud Compute, including the total number of runtime audits, image vulnerabilities, and compliance violations.

The following example command uses curl and basic auth to retrieve the daily stats:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/stats/daily
```
