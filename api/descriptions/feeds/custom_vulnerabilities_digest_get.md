Returns the unique digest for the custom vulnerabilities and associated rules for handling internally created or packaged apps.

### cURL Request

The following cURL command retrieves the digest for the configured custom vulnerabilities.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/feeds/custom/custom-vulnerabilities/digest
```

A successful response will return the digest string.
This is the same value as the `digest` property in the response of the `GET api/v1/feeds/custom/custom-vulnerabilities` endpoint.

