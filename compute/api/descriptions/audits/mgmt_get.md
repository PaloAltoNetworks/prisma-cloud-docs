Changes to any settings (including previous and new values), changes to any rules (create, modify, or delete), and all logon activity (success and failure) are logged. 
These events are called management audits.

This call retrieves a list of all management audits that match the query.

The following example curl command uses basic auth to retrieve all management audits

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/mgmt
```
