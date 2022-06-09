Generates a list of impacted resources for a specific vulnerability.
This endpoint returns a list of all deployed images, registry images, hosts, and serverless functions affected by a given CVE.

Prisma Cloud Compute recalculates the stats for your environment every 24 hours.
Alternatively, you can manually update the stats by clicking the Refresh button in Vulnerability Explorer.

You can use filters such as `cvssThreshold`, `severityThreshold`, or `collections` as query parameters to get desired results.

Consider the following observations:
- You cannot use new filters such as **severityThreshold** and **cvssThreshold** with the **collections** filter or when you're assigned with specific collections or accounts.

**cvssThreshold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of CVSS score or higher.
**severityThreshold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of the severity threshold or higher.
**collections**: Retrieves a list of vulnerabilities (CVEs) that matches the specified collection name.

### cURL Request

Refer to the following example cURL command that retrieves a list of impacted resources for `CVE-2022-28391`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/impacted-resources?cve=CVE-2022-28391'
```

### cURL Request

Refer to the following example cURL command that retrieves a the impacted registry images `CVE-2015-0313` by using an optional query parameter `resourceType`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/impacted-resources?cve=CVE-2015-0313&resourceType=registryImage'
```
**Note**: The API returns the impacted registry images only when you use the optional `resourceType` parameter with value `registryImage`.

### cURL Request

Refer to the following example cURL command that retrieves a paginated list of impacted resources for `CVE-2015-0313` by using optional query parameters `limit` and `offset`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/impacted-resources?cve=CVE-2015-0313&offset=10&limit=100'
```
