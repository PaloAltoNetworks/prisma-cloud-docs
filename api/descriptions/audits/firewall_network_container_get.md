Retrieves all Cloud Native Network Firewall (CNNF) container audits.

Cloud Native Network Firewall (CNNF) is a Layer 3 container-aware virtual firewall that utilizes machine learning to identify valid traffic flows between app components and alert or block anomalous flows. 
CNNF works as an east-west firewall between containers. 
It limits damage by preventing attackers from moving laterally through your environment when they have already compromised one part of it.

```bash
$ curl -k \
  -u <USER> \
  https://<CONSOLE>:8083/api/v1/audits/firewall/network/container
```

