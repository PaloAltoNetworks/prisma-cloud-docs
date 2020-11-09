Retrieves the list of vulnerabilities for internally developed packages.

These entries are used by the Twistlock scanner to detect vulnerable custom components (apps, libraries, etc) that were developed and packaged internally.

**NOTE**: When a vulnerable custom component is detected in an image, you must have a rule to tell Twistlock how to handle it.
Vulnerability rules can be created in the Console UI or with the /api/v1/policies/cve endpoint.
Create a vulnerability rule and set ID 412 (Image contains vulnerable custom components) to ignore, alert, or block.

The following example curl command retrieves the list of custom-defined vulnerabilities:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/feeds/custom/custom-vulnerabilities
```
