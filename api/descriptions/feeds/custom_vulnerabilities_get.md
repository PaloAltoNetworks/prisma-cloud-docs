Retrieves the list of custom vulnerabilities and associated rules for handling internally created or packaged apps.

This list is used by the Prisma Cloud Compute scanner to detect vulnerable custom components (apps, libraries, etc) that were developed and packaged internally.

**Note:** When a vulnerable custom component is detected in an image, you must have a rule to tell Prisma Cloud Compute how to handle it.
Vulnerability rules can be created using the Console UI or with the `/api/v1/vulnerabilty/<RESOURCE-TYPE>` endpoint.
See the `/api/v1/vulnerabilty/<RESOURCE-TYPE>` endpoint for more info.

### cURL Request

The following cURL command retrieves a list of all the custom vulnerabilities and associated rules.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/feeds/custom/custom-vulnerabilities
```

### Response

A successful response will return a list of custom vulnerability rules and the associated digest:

```json
{
	"_id":"customVulnerabilities",
	"rules": [
		{
	      "_id": "<ID>",
	      "package": "internal-lib",
	      "type": "package",
	      "minVersionInclusive": "1.1",
	      "name": "internal-lib",
	      "maxVersionInclusive": "1.8",
	      "md5": ""
	    }
	],
	"digest":"<DIGEST>"
}
```
