Sets the state of trusted images model.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"state":"learning"}'
  https://<CONSOLE>:8083/api/v1/trust/learn
```
