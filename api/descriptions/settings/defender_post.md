This endpoint will allow you to manage the advanced settings from **Manage > Defenders > Manage** page in the console.

The following example curl command uses basic auth to set the local defender API port to `9998`, turn on the Defender runC proxy, and set the number of days to automatically remove disconnected defenders to `4`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"disconnectPeriodDays":4,"listeningPort":9998,"runcProxyEnabled":true}' \
  https://<CONSOLE>:8083/api/v1/settings/defender
```
