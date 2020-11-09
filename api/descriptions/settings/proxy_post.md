Configures the proxy settings.

The following example curl command specifies the proxy to use to access the Internet.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "httpProxy":"http://proxyserver.example.com:8282"
}' \
  https://<CONSOLE>:8083/api/v1/settings/proxy
```
