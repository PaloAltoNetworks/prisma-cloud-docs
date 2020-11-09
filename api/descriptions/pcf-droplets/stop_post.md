This endpoint will instruct the PFC Defenders to stop scanning.

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/pcf-droplets/stop
```
