Returns the full Docker image name for Defender.

Example: `registry-auth.twistlock.com/tw_smbvukudjypnnrqmso0/twistlock/defender:defender_18_11_128`

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/image-name
```
