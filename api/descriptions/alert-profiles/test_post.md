Sends a test alert to verify successful configuration of the alert profile settings.

The following example curl command uses basic auth to send test alert for an email alert profile:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d <REQUEST-PAYLOAD>
  https://<CONSOLE>:8083/api/v1/alert-profiles/test
```

In this case, the `REQUEST-PAYLOAD` would be the full JSON formatted alert profile from the base `GET` command 
