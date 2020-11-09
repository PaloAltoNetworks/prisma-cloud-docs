Returns the digest hash of the CVE allow lists you have configured in Console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/feeds/custom/cve-allow-list/digest
```
