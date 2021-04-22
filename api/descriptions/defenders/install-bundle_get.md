Returns the certificate bundle that Defender needs to securely connect to Console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/install-bundle?consoleaddr=<CONSOLEADDR>
```
