Updates a single role by its name. This endpoint accepts one role at a time, and overrides its entire permissions set.
System role cannot be updated.

Create role.json file (example)
The updated role must contain the "user" permission with read-write access. This permission contains basic API routes required for every authenticated user.

```
[
  {
    "perms": [
        {
            "name": "monitorCI",
            "readWrite": true
        },
        {
            "name": "downloads",
            "readWrite": false
        },
        {
            "name": "accessUI",
            "readWrite": false
        },
        {
            "name": "uIEventSubscriber",
            "readWrite": false
        },
        {
            "name": "user",
            "readWrite": true
        }
    ],
    "name": "runtime manager",
    "description": "runtime manager"
  }
]
```

The following example curl command uses basic auth to update the role:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  --binary-data @role.json \
  https://<CONSOLE>:8083/api/v1/roles
```
