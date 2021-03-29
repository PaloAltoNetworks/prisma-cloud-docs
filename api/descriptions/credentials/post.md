Updates the credentials in the credentials store.
In the Console UI, you can view the credentials store here: **Manage > Authentication > Credential Store**.

Create `credentials.json` file (example):

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

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  --binary-data @credentials.json \
  https://<CONSOLE>:8083/api/v1/credentials
```
