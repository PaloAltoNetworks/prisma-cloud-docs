Specify the learning mode for all host service profiles.

The following example command uses curl and basic auth to specify the learning mode for all host service profiles.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/profiles/service/learn
```
