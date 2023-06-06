Shows the progress of an ongoing regular or on-demand scan of registry.

Use the scan ID from the `/registry/scan` API endpoint to get scan status of the ongoing scan.

### cURL Request

Refer to the following example cURL request that retrieves the ongoing scan details for an on-demand registry scan for repository `alpine` with tag `3.16`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry/progress?onDemand=true&repo=library/alpine&tag=3.16"
```
### cURL Response

Refer to the following example cURL response:

```bash
[
  {
        "discovery": {
            "hostname": "",
            "id": "",
            "scanTime": "0001-01-01T00:00:00Z",
            "type": "",
            "discovery": false,
            "total": 1,
            "scanned": 1,
            "title": "Step 1/2 discovering tags in repository: library/alpine, tag: 3.16"
        },
        "imageScan": {
            "hostname": "",
            "id": "",
            "scanTime": "0001-01-01T00:00:00Z",
            "type": "",
            "discovery": false,
            "total": 1,
            "scanned": 1,
            "title": "Step 2/2 scanning images in repository: library/alpine, tag: 3.16"
        },
        "isScanOngoing": true
    }
]
```