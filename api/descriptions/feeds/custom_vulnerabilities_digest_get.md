Returns the unique digests for all custom vulnerability feeds configured in the console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/feeds/custom/custom-vulnerabilities/digest
```
