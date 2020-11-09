Downloads all serveless scan reports in CSV format.

The following curl command uses basic auth to retrieve a list of all Serverless resources that monitored by Twistlock, and save the results to a CSV file:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/serverless/download \
  > serverless.csv
```
