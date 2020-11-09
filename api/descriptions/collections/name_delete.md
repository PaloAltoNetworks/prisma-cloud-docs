Deletes a collection from the system.

The following example curl command deletes a collection named *my collection*.
Because spaces are considered [unsafe characters in a URL](https://www.ietf.org/rfc/rfc1738.txt), they must be encoded with the value `%20`.

```bash
$ curl -k \
  -u <USER> \
  -X DELETE \
  "https://<CONSOLE>:8083/api/v1/collections/my%20collection"
```
