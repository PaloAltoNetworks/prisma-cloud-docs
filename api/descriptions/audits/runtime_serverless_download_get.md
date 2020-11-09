Returns scan reports in CSV format for any serverless functions you've configured Twistlock to scan.

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o serverless-audits.csv
  https://CONSOLE_ADDRESS:PORT/api/v1/audits/runtime/serverless/download
```
