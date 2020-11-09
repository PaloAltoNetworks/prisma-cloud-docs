Retrieves the digest from the list of suspicious or high risk IP endpoints configured in the console.

The following example curl command retrieves the list of digests:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/feeds/custom/ips/digest
```
