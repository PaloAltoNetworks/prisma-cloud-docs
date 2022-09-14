Returns a protected Fargate task definition for a CloudFormation YAML template given an unprotected task definition.

### cURL Request
Refer to the following example cURL command that accepts the task definition in YAML format for a CloudFormation template:

`<HOSTNAME>` is a single list item from the `/api/v<VERSION>/defenders/names` endpoint.

Unprotected task definition in `unprotected.yaml`

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/yaml' \
  -X POST \
  --data-binary "@unprotected.yaml"
  --output protected.yaml \
  "https://<CONSOLE>/api/v<VERSION>/defenders/fargate.yaml?cloudFormation=true&consoleaddr=<console_address>&filestemMonitoring=false&interpreter=&project=Central+Console"
```

New Protected task will be in `protected.yaml`