Deletes a custom rule.

### cURL Request

Refer to the following example cURL command that deletes a custom rule:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  'https://<CONSOLE>/api/v<VERSION>/custom-rules/{id}'
```

​**Note:** No response will be returned upon successful execution.
