Returns the names of all groups as strings in an array.

```bash
$ curl -X GET \
  https://<CONSOLE>:8083/api/v1/groups/names \
  -u <USER> \
  -H 'Content-Type: application/json' \
```

Sample output:

```
[
    "admins",
    "secops",
    "devops",
    ""
]
```
