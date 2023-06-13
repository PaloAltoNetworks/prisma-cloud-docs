Shows the progress of an ongoing regular or on-demand registry scan. 
By default, the API endpoint displays the progress of a regular scan.

## View regular registry scan progress
For a regular scan, use the API path only without any query parameters.

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
            "total": 4,
            "scanned": 2,
            "title": "Step 1/2 discovering tags in registry us-west2-docker.pkg.dev: Discovered tags in 2/4 repositories with 1 Defenders"
        },
        "imageScan": {
            "hostname": "",
            "id": "",
            "scanTime": "0001-01-01T00:00:00Z",
            "type": "",
            "discovery": false,
            "total": 2,
            "scanned": 0,
            "title": "Step 2/2 scanning images in registry us-west2-docker.pkg.dev: Scanned 0/2 images with 1 Defender"
        },
        "isScanOngoing": true
    }
]
```

## View on-demand registry scan progress

For an on-demand scan that is started using the `/registry/scan` endpoint with the following fields:

- onDemand: (Mandatory) Set the parameter to `true`.
- repo: (Mandatory) Specify the repository name.
- tag: Specify the image tag (alias of image ID).
- digest: Specify the image digest identifier.

> **Note:** You must specify either `tag` or `digest` along with the mandatory parameters `onDemand` and `repo` to view the progress.

### cURL Request

Refer to the following example cURL request that retrieves the ongoing scan details for an on-demand registry scan that is started using the `/registry/scan` endpoint for the repository `alpine` with tag `3.16`:

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
        "isScanOngoing": false
    }
]
```

> **Important:** 
- If you use on-demand scan related parameters such as `registry`, `repo`, or `tag` but set the query parameter `onDemand` to `false`, you'll get a bad request error (400).
- If an on-demand scan was completed and you get the progress response for that scan (i.e. "isScanOngoing": false), the next progress response for that image will be an empty list: `[]`, until you initiate another on-demand scan for that image.