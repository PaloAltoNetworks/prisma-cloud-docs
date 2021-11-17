Set a tag to a CVE.

The following example curl command adds the tag named `ignored` to the CVE `CVE-2017-15088`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "id": "CVE-2017-15088",
   "packageName": "krb5",
   "comment": "my super cool comment"
 }' \
  https://<CONSOLE>:8083/api/v1/tags/ignored/vuln
```
