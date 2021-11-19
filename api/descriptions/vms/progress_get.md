Returns the status of VM image scanning at *Monitor > Vulnerabilities > Hosts > VM images*

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H 'Content-Type: application/json' \
  https://<CONSOLE>:8083/api/v1/vms/progress
```
