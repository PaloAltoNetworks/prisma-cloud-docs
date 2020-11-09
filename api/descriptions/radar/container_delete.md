Deletes a learned connection between two containers.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/radar/container?dstProfileID=sha256:<IMAGE_HASH>&srcProfileID=sha256:<IMAGE_HASH>
```
