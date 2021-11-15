Returns a list of all custom compliance checks.
In the Console UI, custom compliance checks can be found in **Defend > Compliance > Custom**.

The following example curl command gets the list of custom compliance checks:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/custom-compliance
```

Example response:

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
