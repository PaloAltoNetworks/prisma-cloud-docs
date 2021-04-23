Adds or deletes Subject Alternative Name(s) (SANs) in Console's certificate.
Defenders use these names to connect to Console.

SANs are set in a single shot.
You should first retrieve the list of SANs with the GET method.
Then add or remove entries from the `consoleSAN` array, and post the updated JSON object.

The following example curl command uses basic auth to add `node-01.example.com` to the `subjectAltName` field in Console's certificate.

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '
  {
    "consoleSAN": [
      "10.240.0.34",
      "172.17.0.1",
      "ian-23.c.cto-sandbox.internal",
      "127.0.0.1",
      "node-01.example.com"
    ]
  }' \
  https://<CONSOLE>:8083/api/v1/settings/certs
```
