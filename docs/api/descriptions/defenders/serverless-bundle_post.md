Downloads a ZIP file with serverless Defender bundle.

Refer to the following values to assign:
* For `provider`: Use `aws` or `azure`.
* For `runtime`: 
    * If you use `aws`, then you can add the runtime values: `python`, `python3.6`, `python3.7`, `python3.8`, `python3.9`, `nodejs12.x`, `nodejs14.x`, `dotnet6`, `java8`, `java11`, or `ruby2.7`.
    * If you use `azure`, then you can add `dotnet3` or `dotnet6`.

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
  ```