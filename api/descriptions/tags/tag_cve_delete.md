Remove a tag from a CVE.

The following example curl command removes the tag named `ignored` from the CVE `CVE-2017-15088`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  -d \
'{
   "id": "CVE-2017-15088",
   "packageName": "krb5"
 }' \
  https://<CONSOLE>:8083/api/v1/tags/ignored/vuln
```

