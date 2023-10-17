Deletes an alert profile entry by name.
In the request payload, specify the alert profile name. 
This method has no response data.

The following example curl command deletes an existing alert profile named `PROFILE-NAME`.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/alert-profiles/<PROFILE-NAME>
```

