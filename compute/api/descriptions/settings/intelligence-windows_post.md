This endpoint will enable or disable the Windows Intelligence Service from **Manage > System > Intelligence** page in the console.

The following example curl command uses basic auth to enable online updates of Windows vulnerabilities from the intelligence stream:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"windowsFeedEnabled":true}' \
  https://<CONSOLE>:8083/api/v1/settings/intelligence-windows
```
