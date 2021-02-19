Changes a user's password (the user that is invoking the API).

The following example command uses curl and basic auth to replace `<USER>` password with `<NEWPASSWORD>`:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d '{"oldPassword": "<OLDPASSWORD>", "newPassword": "<NEWPASSWORD>"}' \
  https://<CONSOLE>:8083/api/v1/users/password
```
