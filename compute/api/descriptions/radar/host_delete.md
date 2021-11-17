Deletes a learned connection between two apps in CNNF for hosts.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X DELETE \
  https://<CONSOLE>:8083/api/v1/radar/host?dstProfileID=<APP>&srcProfileID=<APP>
```
