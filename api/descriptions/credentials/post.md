This endpoint will allow for update of the credentials found with the app here **Manage > Authentication > Credential Store**

Create credentials.json file (example)

```json
[
  {
    "_id": "Sample",
    "type": "basic",
    "accountID": "username",
    "secret": {
      "plain": "password"
    }
  }
]
```

The following example curl command uses basic auth to update the checks:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  --binary-data @credentials.json \
  https://<CONSOLE>:8083/api/v1/credentials
```
