Returns the status of the registry scans.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v<VERSION>/statuses/registry
```
### Response

```json
{
  "scanTime": "2019-07-31T19:42:49.036311567Z",
  "completed": true
}
```