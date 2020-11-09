Retrieve a list of only the names of all alert profiles created in the system.

The following example curl command uses basic auth to retrieve all alert profiles' names:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/alert-profiles/names
```

Example Response:

```
[
    "jira",
    "aqsa vulns"
]
```
