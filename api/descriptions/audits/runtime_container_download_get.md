Downloads the runtime container audit logs in csv format.

A call to this api endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/audits/runtime/container/download
  > conatiner_audits.csv
```
