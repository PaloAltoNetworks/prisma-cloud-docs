Bans a custom list of suspicious or high-risk IP addresses.

**Note:** Any previously installed lists are overwritten.

### cURL Request

The following cURL command installs a custom list of banned suspicious or high-risk IP addresses.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"name":"banned-ips", "feed":["193.171.1.1","193.171.1.2"]}' \
  https://<CONSOLE>/api/v1/feeds/custom/ips
```

**Note:** No response will be returned upon successful execution.

To confirm the IPs have been added to the ban list, invoke the `GET /api/v1/feeds/custom/ips` endpoint.

