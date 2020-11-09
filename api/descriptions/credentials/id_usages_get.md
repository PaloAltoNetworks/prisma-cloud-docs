This endpoint will return a list in json format of all the usages of credentials found with the app here **Manage > Authentication > Credential Store**

The following example curl command uses basic auth to return:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/credentials/Sample/usages
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
