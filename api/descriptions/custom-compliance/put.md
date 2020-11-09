This endpoint will allow for update of the custom compliance checks on page **Defend > Compliance > Custom**

Create custom_check.json file (example)

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

The following example curl command uses basic auth to update the checks:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  --binary-data @custom_check.json \
  https://<CONSOLE>:8083/api/v1/custom-compliance
```
