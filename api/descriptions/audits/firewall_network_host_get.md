Retrieves all Cloud Native Network Firewall (CNNF) audits. 
These are based on violations of CNNF policies defined under Defend > Firewalls > Cloud Native Network Firewall.
Click [here](https://docs.twistlock.com/docs/latest/firewalls/cnnf.html#overview) to learn more about CNNF.

The following example uses basic auth to retrieve all application firewall audits.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/firewall/network/host
```

