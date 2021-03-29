Retrieves the globally allow-listed Common Vulnerabilities and Exposures (CVE).

### cURL Request

The following cURL command retrieves the globally allow-listed CVEs.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/feeds/custom/cve-allow-list
```

### Response

A successful response returns all CVEs globally allow-listed.

```json
{
	"_id":"cveAllowList",
	"rules": [
		{
			"cve": "CVE-2018-2222",
			"expiration": "2020-06-18T00:00:00Z"
		}
	],
	"digest":"<DIGEST>"
}
```
