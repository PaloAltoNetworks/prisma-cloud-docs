Deletes a specific custom compliance check.

This endpoint maps to **Defend > Compliance > Custom** in the Console UI.

### cURL Request

Refer to the following example cURL command that uses basic auth to delete the compliance check with id 9000:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>/api/v<VERSION>/custom-compliance/9000
```
