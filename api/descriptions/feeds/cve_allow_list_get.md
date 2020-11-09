Retrieves the list of globally whitelisted CVEs.

The following example curl command retrieves a list of globally whitelisted CVEs:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/feeds/custom/cve-allow-list
```
