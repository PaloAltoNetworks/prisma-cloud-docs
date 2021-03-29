Upgrades all connected single Linux Container Defenders.

This does not update cluster Container Defenders (such as Defender DaemonSets), Serverless Defenders, or Fargate Defenders.
To upgrade cluster Container Defenders, redeploy them.
To upgrade Serverless and Fargate Defenders, re-embed them.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/defenders/upgrade
```
