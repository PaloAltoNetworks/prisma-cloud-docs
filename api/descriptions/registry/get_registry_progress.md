Shows the progress of an ongoing regular or on-demand scan of the number of images out of the total number of images in a registry. 
By default, the API endpoint displays the progress of a regular scan.

## View regular registry scan progress
For a regular scan, use the API path only without the query parameters.

### cURL Request

Refer to the following example cURL request that retrieves the ongoing scan details for a regular registry scan:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/registry/progress"
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
            "total": 2,
            "scanned": 2,
            "title": ""
        },
        "imageScan": {
            "hostname": "",
            "id": "",
            "scanTime": "0001-01-01T00:00:00Z",
            "type": "",
            "discovery": false,
            "total": 1,
            "scanned": 1,
            "title": ""
        },
        "isScanOngoing": false
    }
]
```

## View on-demand registry scan progress

For on-demand scan, use the following query parameters with the same values as used to trigger the on-demand scan in the API endpoint `/registry/scan`:

- onDemand: (Mandatory) Set the parameter to `true`.
- repo: (Mandatory) Specify the repository name.
- tag: Specify the image tag (alias of image ID).
- digest: Specify the image digest identifier.

> **Note:** You must specify either `tag` or `digest` along with the mandatory parameters `onDemand` and `repo` to view the progress.

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

> **Important:** 
- If you use on-demand scan related parameters such as `registry`, `repo`, or `tag` but set the query parameter `onDemand` to `false`, you'll get an empty response.
- If you view the on-demand scan result once and try to retrieve the progress again, you will get an empty response unless you initiate another on-demand scan.