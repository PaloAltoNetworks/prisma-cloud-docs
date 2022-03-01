Although this is a supported endpoint, it’s not versioned. 
For more information about supported and versioned endpoints, see [Stable endpoints](https://prisma.pan.dev/docs/cloud/cwpp/stable-endpoints)

Scans AWS EC2 instances for vulnerabilities without the need to install an agent.

### cURL Request

Refer to the following example cURL command that scans AWS EC2 instances:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  "https://<CONSOLE>/api/v1/agentless/scan"
```