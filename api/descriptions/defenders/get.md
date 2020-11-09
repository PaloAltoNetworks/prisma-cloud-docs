Lists all deployed Defenders.

The following command uses basic authorization to retrieve a list of all deployed Defenders along with metadata

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders
```

