Generates a list of impacted resources for a specific vulnerability.
This endpoint returns a list of all deployed images, registry images, hosts, and serverless functions affected by a given CVE.

Prisma Cloud Compute recalculates the stats for your environment every 24 hours.
Alternatively, you can manually update the stats by clicking the Refresh button in Vulnerability Explorer.

You can use filters such as `cvssThreshold`, `severityThreshold`, or `collections` as query parameters to get desired results.

Consider the following observations:
- You cannot use new filters such as **severityThreshold** and **cvssThreshold** with the **collections** filter or when you're assigned with specific collections or accounts.

* **cvssThresold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of CVSS score or higher.
* **severityThreshold**: Retrieves a list of vulnerabilities (CVEs) that matches the specified value of the severity threshold or higher.
* **collections**: Retrieves a list of vulnerabilities (CVEs) that matches the specified collection name.

### cURL Request

Refer to the following example cURL command that retrieves a list of impacted resources for `CVE-2022-28391`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/stats/vulnerabilities/impacted-resources?cve=CVE-2022-28391'
```
### cURL Response

Refer to the following example JSON response that shows the risk tree for the impacted resources:

```bash
{
  "_id": "CVE-2022-28391",
  "images": [
    {
      "resourceID": "sha256:a787cb9865032e5b5a407ecdf34b57a23a4a076aaa043d71742ddb6726ec9229",
      "containers": [
        {
          "image": "alpine:3.11",
          "container": "mystifying_banzai",
          "host": "jen-sle12-dock-0911t162051-cont-def-pre-lngcon231.c.twistlock-test-247119.internal",
          "factors": {
            "rootPrivilege": true
          }
        },
        {
          "image": "alpine:3.11",
          "container": "compassionate_austin",
          "host": "jen-sle15-dock-0911t162051-cont-def-pre-lngcon231.c.twistlock-test-247119.internal",
          "factors": {
            "rootPrivilege": true
          }
        },
        ...
    },
    {
      "resourceID": "sha256:fcd5d51fc526ef1ff7cf2e94aa91be39d052874057ff603b66b9b461386fae93",
      "containers": [
        {
          "image": "infoslack/dvwa:latest",
          "factors": {}
        }
      ]
    },
    {
      "resourceID": "sha256:bc6b65772f298854ea0dca7d562684cb835f2f677e0e2ea1863b4566f29dcac1",
      "containers": [
        {
          "image": "ghcr.io/christophetd/log4shell-vulnerable-app:latest",
          "factors": {}
        }
      ]
    },
    ...
  ],
  "hosts": [
    {
      "resourceID": "jen-ubu2204-dock-0911t162051-cont-def-pre-lngcon231.c.twistlock-test-247119.internal"
    },
    {
      "resourceID": "jen-ubu2004-dock-0911t162051-cont-def-pre-lngcon231.c.twistlock-test-247119.internal"
    },
    ...
  ],
  "imagesCount": 5,
  "hostsCount": 21,
  "functionsCount": 0,
  "codeReposCount": 0,
  "registryImagesCount": 0
}
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