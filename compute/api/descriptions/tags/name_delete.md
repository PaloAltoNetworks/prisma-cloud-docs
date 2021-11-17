Deletes a tag from the system.

The following example curl command deletes a tag named *my tag*.
Because spaces are considered [unsafe characters in a URL](https://www.ietf.org/rfc/rfc1738.txt), they must be encoded with the value `%20`.

```bash
$ curl -k \
  -u <USER> \
  -X DELETE \
  "https://<CONSOLE>:8083/api/v1/tags/my%20tag"
```
