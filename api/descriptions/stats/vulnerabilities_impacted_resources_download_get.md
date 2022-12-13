Downloads a list of impacted resources for a specific vulnerability in a CSV format.
This endpoint returns a list of all deployed images, registry images, hosts, and serverless functions affected by a given CVE.

You can use filters such as `cvssThreshold`, `severityThreshold`, or `collections` as query parameters to get desired results.

Consider the following observations:
- You cannot use new filters such as **severityThreshold** and **cvssThreshold** with the **collections** filter or when you're assigned with specific collections or accounts.

* **cvssThresold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of CVSS score or higher.
* **severityThreshold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of the severity threshold or higher.
* **collections**: Retrieves a list of vulnerabilities (CVEs) that matches the specified collection name.

### cURL Request

Refer to the following example cURL command that downloads a list of impacted resources for `CVE-2015-0313` in a CSV format:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o <FILE NAME> \
  "https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/impacted-resources/download?cve=CVE-2015-0313"
```