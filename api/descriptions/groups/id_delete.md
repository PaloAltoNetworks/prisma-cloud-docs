Deletes a group from the system. The id's can be retrieved with a GET from the /group/ api endpoint.

A call to this api endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/groups
```
