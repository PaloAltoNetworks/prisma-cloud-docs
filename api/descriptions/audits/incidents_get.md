Twistlock analyzes individual audits and correlates them together to surface unfolding attacks.
These chains of related audits are called incidents. 
This endpoint retrieves a list of incidents that are not acknowledged (not in archived state).

The following example curl command lists all incidents.

```bash
$ curl -k \
  -u <USER> \
  https://console:8083/api/v1/audits/incidents
```

