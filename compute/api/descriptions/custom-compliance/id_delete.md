This endpoint will delete a specific custom compliance check on page **Defend > Compliance > Custom**


The following example curl command uses basic auth to delete check with id 9000:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/custom-compliance/9000
```
