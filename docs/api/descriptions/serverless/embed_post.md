The following curl command uses basic auth to retrieve a list of all Serverless resources that monitored by Prisma Cloud Compute, and save the results to a CSV file:

```bash
$ curl -k \
  -X POST \
  -H "Content-Type: application/octet-stream" \
  -u <USER> \
  --data-binary @<PATH_TO_ZIP> \
  'http://<CONSOLE>:8083/api/v1/serverless/embed?runtime=<python3.6>&handler=<main.handler>&function=<functionName>' \
  -o twistlock_lambda.zip
```
