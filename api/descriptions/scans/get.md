Retrieves all scan reports for images scanned by the Jenkins plugin or twistcli tool.
In Console, this information is found in **Monitor > Vulnerabilities > Images > CI**.

[//]: # (https://github.com/twistlock/twistlock/issues/16586)

Note that the `discovered` field for each compliance finding (`info > allCompliance > compliance > discovered`) doesn't contain valid data and will be removed in a future release.

The following example curl command uses basic auth to retrieve the scan report for all images scanned using the Jenkins CI plugin or the twistcli tool.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/scans
```

To get the report of a specific scan, you can add query parameters to narrow the scope of the request.

The following example curl command uses basic auth to retrieve the scan report for just an image with a SHA256 ID of `sha256:f756e84300d8e53006090573dd33abe5b8cfac3e42d104fc4be37f435fe512f3`.
 
```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/scans?imageID=sha256:f756e84300d8e53006090573dd33abe5b8cfac3e42d104fc4be37f435fe512f3
```
