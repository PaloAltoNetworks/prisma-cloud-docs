Creates an augmented Dockerfile with Defender and dependencies included as a ZIP file.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
 '{
    "appID": "my-app",
    "consoleAddr": "https://localhost:8083",
    "dataFolder": "/var/lib/docker/containers/twistlock/tmp",
    "dockerfile": "/var/lib/docker/overlay2/183e9e3ec933ba2363bcf6066b7605d99bfcf4dce84f72eeeba0f616c679cf48"
  }' \
  "https://<CONSOLE>/api/v<VERSION>/defenders/app-embedded"
```