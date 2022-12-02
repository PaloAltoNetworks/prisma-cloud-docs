Stops an ongoing scan on hosts or containers for vulnerabilities and compliance.

### cURL Request

Refer to the following example cURL command:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  “https://<CONSOLE>/api/v<VERSION>/agentless/stop”
```