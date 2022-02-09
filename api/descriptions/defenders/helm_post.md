Creates a Helm deployment file that you can use to deploy Defenders to your cluster.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -o twistlock-defender-helm.tar.gz \
  -d \
  '{
   "orchestration": "container",
   "consoleAddr": "servo-vmware71",
   "namespace": "twistlock"
   }' \
  "https://<CONSOLE>/api/v<VERSION>/defenders/helm/twistlock-defender-helm.tar.gz"
```