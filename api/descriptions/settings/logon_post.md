Configures the timeout for Console sessions.

The following example curl command uses basic auth to set the timeout to 900 seconds (15 minutes).

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '{"sessionTimeoutSec": 900}' \
  https://<CONSOLE>:8083/api/v1/settings/logon
```
