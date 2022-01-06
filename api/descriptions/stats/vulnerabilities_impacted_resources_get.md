Generates a risk tree, which is a map of your exposure to a specific vulnerability.
This endpoint returns a list of all images and containers affected by a given CVE.

The data in this endpoint is updated every time a scan runs.
By default, Prisma Cloud Compute rescans your environment every 24 hours.
Alternatively, you can manually update the stats by clicking the Refresh button in Vulnerability Explorer.

The following example command retrieves a risk tree for `CVE-2015-0313`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/vulnerabilities/impacted-resources?cve=CVE-2015-0313
```
