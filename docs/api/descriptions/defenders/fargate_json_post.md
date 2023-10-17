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
Refer to the following example cURL command that accepts the task definition in JSON format for a CloudFormation template:

`<HOSTNAME>` is a single list item from the `/api/v<VERSION>/defenders/names` endpoint.

Unprotected task definition in `unprotected.json`

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  --data-binary "@unprotected.json"
  --output protected.json \
  "https://<CONSOLE>/api/v<VERSION>/defenders/fargate.json?cloudFormation=true&consoleaddr=<console_address>&filestemMonitoring=false&interpreter=&project=Central+Console"
```

### cURL Response
New Protected task will be in `protected.json`