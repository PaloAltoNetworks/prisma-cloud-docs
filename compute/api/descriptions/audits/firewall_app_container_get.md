Retrieves all Cloud Native Application Firewall (CNAF) audits. 
These are based on violations of CNAF policies defined under Defend > Firewalls > Cloud Native App Firewall.
Click [here](https://docs.twistlock.com/docs/latest/firewalls/cnaf.html#overview) to learn more about CNAF.

The following example uses basic auth to retrieve all application firewall audits.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/firewall/app/container
```

