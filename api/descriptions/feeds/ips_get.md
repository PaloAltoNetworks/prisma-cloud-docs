Retrieves the custom list of blacklisted IP addresses.

The following example curl command retrieves the custom list of blacklisted IP addresses:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/feeds/custom/ips
```
