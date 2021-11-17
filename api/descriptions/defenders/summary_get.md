List the number of Defenders in each defender category.

The following command uses basic authorization to retrieve a summary of Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/defenders/summary
```

