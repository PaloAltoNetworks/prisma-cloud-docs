Retrieves the digest string for the Common Vulnerabilities and Exposures (CVE) allow list configured in Console.

### cURL Request

The following cURL command retrieves the digest for the configured CVE allow list.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/feeds/custom/cve-allow-list/digest
```

A successful response will return the digest string. This is the same value as the `digest` property in the response of the `GET api/v1/feeds/custom/cve-allow-list` endpoint.

