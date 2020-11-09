This endpoint will allow you to enable or disable telemetry. You can find more about this in our [telemetry](https://docs.twistlock.com/docs/latest/technology_overviews/telemetry.html#disabling-telemetry) article.

The following example curl command uses basic auth to turn off telemetry:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"enabled":false}' \
  https://<CONSOLE>:8083/api/v1/settings/telemetry
```
