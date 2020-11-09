This endpoint will delete all serverless runtime audits.

The following example curl command uses basic auth to delete the current audits:


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/audits/runtime/serverless
```

