Downloads a list of vulnerabilities (CVEs) in the deployed images, registry images, hosts, and serverless functions affecting your environment in a CSV format.

The response also includes detailed descriptions for each CVE. The data for each CVE, such as impacted packages, highest severity, and so on, is based on the entire environment irrespective of the collections filter, assigned collections, or assigned accounts.

You can use filters such as `cvssThreshold`, `severityThreshold`, or `collections` as query parameters to get desired results.

Consider the following observations:
- You cannot use new filters such as **severityThreshold** and **cvssThreshold** with the **collections** filter or when you're assigned with specific collections or accounts.
- The impacted resources and distribution counts are not retrieved when you apply filters or you are assigned with specific collections or accounts. For example, when you apply these filters, the counts in the API `/stats/vulnerabilities` are returned as zero and empty in the API `/stats/vulnerabilites/download`.

* **cvssThresold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of CVSS score or higher.
* **severityThreshold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of the severity threshold or higher.
* **collections**: Retrieves a list of vulnerabilities (CVEs) that matches the specified collection name.

### cURL Request

Refer to the following example cURL command that downloads a summary count of the CVEs and detailed descriptions for each CVE in a CSV format:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  - o <FILE NAME> \
  'https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/download'
```