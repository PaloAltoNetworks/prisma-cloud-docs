Shows the progress of an ongoing regular or on-demand scan of registry.

Set the query parameter `onDemand` to `true` to view the progress of on-demand scans. By default, the API endpoint shows the progress of a regular scan.

> **NOTE:** If you use `onDemand` related parameters such as `registry`, `repo`, or `tag` but set `onDemand` to `false`, you'll get an empty response.

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