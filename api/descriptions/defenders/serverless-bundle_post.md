Downloads a ZIP file with serverless Defender bundle.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/octet-stream' \
  -o serverless_bundle.zip \
  -X POST \
  -d '{"provider": ["aws"], "runtime": ["nodejs14.x"]}' \
  "https://<CONSOLE>/api/v<VERSION>/defenders/serverless/bundle"