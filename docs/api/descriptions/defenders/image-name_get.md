Returns the full Docker image name for Defender.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/defenders/image-name
```

### Response

Refer to the following example cURL response:

`registry-auth.twistlock.com/tw_mcxweebesog0apjuhtmatv7saf9xdnwd/twistlock/defender:defender_21_11_812`
