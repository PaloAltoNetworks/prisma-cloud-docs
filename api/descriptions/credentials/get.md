This endpoint will return a list in json format of the credentials found with the app here **Manage > Authentication > Credential Store**

The following example curl command uses basic auth to return:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/credentials
```
