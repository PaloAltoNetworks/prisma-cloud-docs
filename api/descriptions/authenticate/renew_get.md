Renews an old (unexpired) access token by returning a new one.

The following example curl command retrieves a new access token:

```bash
$ curl -k \
  -H "Authorization: Bearer <OLD_ACCESS_TOKEN> \
   https://<CONSOLE>:8083/api/v1/authenticate/renew
```
