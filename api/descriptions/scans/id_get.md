Retrieves all scan reports for images scanned by the Jenkins plugin or twistcli tool for a specific image with an given `id`. The `id` is `_id` value returned in the base `/api/v1/scans` request.

The following example curl command uses basic auth to retrieve the scan report for just an image with a SHA256 ID of `5c3385fd2e76c5c16124c077`.
 
```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/scans/5c3385fd2e76c5c16124c077"
```