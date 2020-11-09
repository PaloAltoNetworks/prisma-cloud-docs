Retrieves CVEs from the vulnerability database grouped into distribution where you will see a count for vulnerabilities per distribution.

The following example curl command uses basic auth to retrieve this data:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/cves/distribution
```
