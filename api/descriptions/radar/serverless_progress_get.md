Returns the scan progress from Console's Radar page (serverless view).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/radar/serverless/progress
```

Example of the return data:

```json
[
  {
    "hostname": "",
    "id": "",
    "type": "serverlessRadar",
    "discovery": false,
    "total": 1,
    "scanned": 1,
    "title": ""
  }
]
```
