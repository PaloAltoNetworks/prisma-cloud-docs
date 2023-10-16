Returns the certificate bundle that Defender needs to securely connect to Console.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/defenders/install-bundle?consoleaddr=<CONSOLEADDR>"
```

<CONSOLEADDR> is the hostname of the Console.
