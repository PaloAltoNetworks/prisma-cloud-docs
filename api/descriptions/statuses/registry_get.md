Returns the status of the registry scans.


```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/statuses/registry
```
Here is an example of what is returned:

```json
{
  "scanTime": "2019-07-31T19:42:49.036311567Z",
  "completed": true
}
```