Updates a deployed Defender's configuration.

`<HOSTNAME>` is a single list item from the `/api/v1/defenders/names` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"proxyListenerType": "tcp", "registryScanner":"<true|false>", "serverlessScanner":"<true|false>"}' \
  https://<CONSOLE>/api/v<VERSION>/defenders/<HOSTNAME>/features
```

