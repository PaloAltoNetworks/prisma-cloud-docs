Returns the names of all groups as strings in an array.

A curl command to access this endpoint may resemble the following code snippet:

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
