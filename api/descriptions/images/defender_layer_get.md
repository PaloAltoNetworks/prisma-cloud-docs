Returns the the Twistlock Defender in as a layer that can be used in an AWS Lambda implementation.

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H "Content-Type: application/octet-stream" \
  -o twistlock_defender_layer.zip \
  https://<CONSOLE>:8083/api/v1/images/twistlock_defender_layer.zip
```
