Specifies a list of CVEs to globally whitelist.
Any previously installed list is overwritten.

The following example command uses curl and basic auth to install a list of globally whitelisted CVEs.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \
'{
  "rules": [
    {
      "cve": "CVE-2018-2222",
      "expiration": "2020-06-18T00:00:00Z"
    }
  ]
}' \
  https://<CONSOLE>:8083/api/v1/feeds/custom/cve-allow-list
```
