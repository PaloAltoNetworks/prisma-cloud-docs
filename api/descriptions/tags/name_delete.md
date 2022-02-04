Deletes a tag from the system.

### cURL Request

Refer to the following example cURL command that deletes a tag named *my tag*:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  "https://<CONSOLE>/api/v<VERSION>/tags/my%20tag"
```
A space must be encoded with the value `%20` as specified here in [unsafe characters in a URL](https://www.ietf.org/rfc/rfc1738.txt).