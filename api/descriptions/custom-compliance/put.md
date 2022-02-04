This endpoint will allow for update of the custom compliance checks.

This endpoint maps to **Defend > Compliance > Custom** in the Console UI.

### cURL Request

Create `custom_check.json` file (example):

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
Refer to the following example curl command that uses basic auth to update the checks:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d @custom_check.json \
  https://<CONSOLE>/api/v<VERSION>/custom-compliance
```
