Returns a list of all custom compliance checks.

This endpoint maps to **Defend > Compliance > Custom** in the Console UI.

### cURL Request

Refer to the following example curl command that gets the list of custom compliance checks:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/custom-compliance
```

### Response

```
[
  {
    "modified": "2019-03-07T17:01:12.355Z",
    "owner": "pierre",
    "name": "apitest",
    "previousName": "",
    "_id": 9000,
    "title": "apitest",
    "script": "if [ $(stat -c %a /bin/busybox) -eq 755 ]; then\n echo 'test permission failure' && exit 1;\nfi",
    "severity": "high"
  }
]
```
