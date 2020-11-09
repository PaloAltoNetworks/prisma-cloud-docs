This endpoint will delete a specific credentials found with the app here **Manage > Authentication > Credential Store**


The following example curl command uses basic auth to delete check with id "Sample":

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/credentials/Sample
```

Below is an example of a credential that was added with the GET endpoint.

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

