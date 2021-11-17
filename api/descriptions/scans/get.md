Retrieves all scan reports for images scanned by the Jenkins plugin or twistcli.

This endpoint maps to the image table in **Monitor > Vulnerabilities > Images > CI** in the Console UI.

### cURL Request

The following cURL command retrieves the scan reports for all images scanned using the Jenkins CI plugin or the twistcli tool.

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/scans
```

To get the report of a specific scan, add query parameters to narrow the scope of the request.

The following cURL command retrieves the scan report for an image with a SHA256 ID of `sha256:f756e84300d8e53006090573dd33abe5b8cfac3e42d104fc4be37f435fe512f3`.
 
```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/scans?imageID=sha256:f756e84300d8e53006090573dd33abe5b8cfac3e42d104fc4be37f435fe512f3
```

A successful response returns the scan reports.
