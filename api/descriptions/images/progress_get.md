Returns the status of image scanning at *Monitor > Vulnerabilities > Images*

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H 'Content-Type: application/json' \
  https://<CONSOLE>:8083/api/v1/images/progress
```
