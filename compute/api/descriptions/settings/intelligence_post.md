Configures the Intelligence Stream.

The following example curl command uses basic auth to configure settings of your Intelligence Stream.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
  '{
   "windowsFeedEnabled": true,
   "enabled": true,
   "address": "https://intelligence.twistlock.com",
   "token": "<TOKEN>",   
}' \
  https://<CONSOLE>:8083/api/v1/settings/intelligence
```
