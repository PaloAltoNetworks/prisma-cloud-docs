Retrieves a list of deployed Defender DaemonSets.
You must specify a `credentialID`, of type `kubeconfig`, which identifies your cluster and user.
Credentials are managed in Console's credentials store (`/api/v1/credentials`).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/deployment/daemonsets?credentialID=<CREDENTIAL NAME>
```
