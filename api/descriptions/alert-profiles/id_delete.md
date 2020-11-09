Deletes an alert profile entry by name.
In the request payload, specify the alert profile name. 
This method has no response data.

The following example curl command uses basic auth to delete an existing alert profile entry, where **aqsa** is an alert profile name which is being deleted.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/alert-profiles/aqsa
```

