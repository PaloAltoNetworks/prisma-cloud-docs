Deploys a Defender DaemonSet to the cluster identified by `credentialID`.
The `credentialID`, of type `kubeconfig`,  must exist before calling this endpoint.
It identifies the cluster's API server, user, and credentials.

Use the various request parameters to control the properties of the deployed DaemonSet.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
      "credentialID": "",
      "consoleAddr": "",
      "namespace": "",
      "orchestration": "",
      "...":"..."
      }' \
  https://<CONSOLE>:8083/api/v1/deployment/daemonsets/deploy
```
