Lists the number of Defenders in each defender category.


### cURL Request

Refer to the following example cURL command that retrieves a summary of Defenders:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/defenders/summary
```

