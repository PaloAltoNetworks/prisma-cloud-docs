Deletes **all** access audits. This deletion cannot be undone. 


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://console:8083/api/v1/audits/access
```
