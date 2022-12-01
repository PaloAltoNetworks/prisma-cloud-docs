Scans the hosts or containers for vulnerabilities and compliance.

**Before you begin**
Make sure that you download (use the agentless/templates API) and apply the permission templates in the supported cloud accounts: AWS, Azure, GCP, and OCI.


### cURL Request

Refer to the following example cURL command:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  “https://<CONSOLE>/api/v<VERSION>/agentless/scan”
```