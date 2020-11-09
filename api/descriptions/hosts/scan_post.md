Re-scan all hosts immediately.

The following example command uses curl and basic auth to force Twistlock to re-scan all hosts

```bash
$ curl -k \
  -u <USER> \
  -X POST \
  https://<CONSOLE>:8083/api/v1/hosts/scan
```
