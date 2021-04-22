Deletes an image trust group. Specify the image trust group to be deleted by the `_id`.

The following example curl command uses basic auth to specify a image trust group for deletion with the handle `docker-ubuntu-group`.


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/trust/docker-ubuntu-group
```
