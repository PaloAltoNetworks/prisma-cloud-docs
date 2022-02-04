Returns a protected Fargate task definition given an unprotected task definition.

### cURL Request
Refer to the following example cURL command:

`<HOSTNAME>` is a single list item from the `/api/v<VERSION>/defenders/names` endpoint.

Unprotected task definition in `unprotected.json`

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  --data-binary "@unprotected.json"
  --output protected.json \
  "https://<CONSOLE>/api/v<VERSION>/defenders/fargate.json?consoleaddr=<HOSTNAME>&defenderType=appEmbedded"
```

New Protected task will be in `protected.json`
