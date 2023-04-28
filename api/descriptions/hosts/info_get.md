Returns minimal information that includes hostname, distro, distro-release, collections, clusters, and agentless about all deployed hosts.

A curl command to access this endpoint may resemble the following code snippet:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/hosts/info
```
