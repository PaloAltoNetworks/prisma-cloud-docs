Adds a group to the system, or updates an existing one.

The following example command uses curl and basic auth to create a new group with two users.
Note that the values for `lastModified`, `owner`, and `_id` do not need to be specified.
They are automatically filled in by the system.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"groupName": "wonks", "user": [{"username": "ian"},{"username": "toad"}],"ldapGroup": false,"samlGroup": false,"role": "admin"}' \
  https://<CONSOLE>:8083/api/v1/groups
```
