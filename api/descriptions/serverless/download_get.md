Downloads all serverless scan reports in CSV format.

The following curl command retrieves a list of all serverless resources monitored by Twistlock and saves the results in a CSV file:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/serverless/download \
  > serverless.csv
```
