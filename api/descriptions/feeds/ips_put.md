Specifies a custom list of banned IP addresses.

Any previously installed list is overwritten.

The following example command uses curl and basic auth to install a custom list of banned IP addresses:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"name":"banned-ips", "feed":["193.171.1.1","193.171.1.2"]}' \
  https://<CONSOLE>:8083/api/v1/feeds/custom/ips
```
