Creates a DaemonSet deployment file in YAML format that you can use to deploy Defender to your cluster.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
 '{
   "orchestration": "container",
   "consoleAddr": "servo-vmware71",
   "namespace": "twistlock"
  }' \
  "https://<CONSOLE>/api/v<VERSION>/defenders/daemonset.yaml"
```