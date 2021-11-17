This endpoint will report if "Anonymously report threats and vulnerabilities to Prisma Cloud Compute" is enabled in the console or not. You can find more about this in our [telemetry](https://docs.twistlock.com/docs/latest/technology_overviews/telemetry.html#disabling-telemetry) article.

The following curl command uses basic auth to retrieve whether or not telemetry is enabled or not:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/telemetry
```
