Returns a protected Fargate task definition given an unprotected task definition.


`<HOSTNAME>` is a single list item from the `/api/v1/defenders/names` endpoint.

Unprotected task definition in `unprotected.json`

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  --data-binary "@unprotected.json"
  --output protected.json
  https://<CONSOLE>:8083/api/v1/defenders/fargate.json?consoleaddr=<HOSTNAME>&defenderType=appEmbedded
```

New Protected task will be in `protected.json`
