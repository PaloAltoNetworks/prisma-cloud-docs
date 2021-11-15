Updates the properties of an existing trusted image entry.

In the request payload, specify either the `_id` or image name.
The trusted group ID needs to be specified in request payload.

On success, this method returns the handle (unique ID) for the modified entry.
For more information about handles, see the `_id` in the response body for the GET method.

The following example curl command uses basic auth to modify the image property for an existing trusted image entry, where the handle for the entry is `docker-ubuntu-group`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"image":"ubuntu/18.04", "_id":"docker-ubuntu-group"}' \
  https://<CONSOLE>:8083/api/v1/trust/docker-ubuntu-group
```
