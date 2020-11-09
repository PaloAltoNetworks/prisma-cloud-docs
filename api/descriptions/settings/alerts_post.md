Configure alerts.

The following example curl command sets the aggregation period for alerts to one hour.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "aggregationPeriodMs": 3600000,
   "consoleAddress": "https://<CONSOLE>:8083",
   "securityAdvisorWebhook": ""   
}' \
  https://<CONSOLE>:8083/api/v1/settings/alerts
```
