Retrieves the digest string for the list of suspicious or high risk IP endpoints configured in Console.

### cURL Request

The following cURL command retrieves the digest for the banned suspicious or high-risk IP addresses.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/feeds/custom/ips/digest
```

A successful response will return the digest string. This is the same value as the `digest` property in the response of the `GET api/v1/feeds/custom/ips` endpoint.

