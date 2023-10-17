Removes a tag from a vulnerability.
When you delete a tag, the tag is deleted from a wider scope. All the packages and resources that were in scope will be untagged.

### cURL Request

Refer to the following example cURL command that removes the tag named `ignored` from the CVE `CVE-2017-15088`:

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
  "https://<CONSOLE>/api/v<VERSION>/tags/ignored/vuln"
```

