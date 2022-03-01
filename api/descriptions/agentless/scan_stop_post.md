Although this is a supported endpoint, it’s not versioned. 
For more information about supported and versioned endpoints, see [Stable endpoints](https://prisma.pan.dev/docs/cloud/cwpp/stable-endpoints)

Stops the ongoing agentless scans of the AWS EC2 instances for vulnerabilities.

### cURL Request

Refer to the following example cURL command that stops the agentless scan of the AWS EC2 instances:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  "https://<CONSOLE>/api/v1/agentless/stop"
```