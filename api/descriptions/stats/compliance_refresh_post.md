Refreshes the current day's list and counts of compliance issues, as well as the list of affected running resources.

This endpoint returns the same response as `/api/v<VERSION>/stats/compliance`, but with updated data for the current day.

### cURL Request

Refer to the following example cURL command that refreshes compliance statistics for the current day:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  'https://<CONSOLE>/api/v<VERSION>/stats/compliance/refresh'
```
A successful response returns a summary count of compliance issues for the current day. The response also shows a detailed list of compliance issues for each running container and host for the current day.
