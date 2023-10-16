Updates the list of VM image scan scopes.
The list of scopes are updated in a single shot.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > Vulnerabilities > Hosts > VM images**.
2. Under the **VM images scope** table, add a registry item using **+ Add scope**.

   **Note:** If the **+ Add scope** button is not present, use the **Add the first item** link.

3. Click the **Save** button.

### General Set up and Scan Process

This endpoint works hand-in-hand with the `/policies` endpoints.
Prisma Cloud auto-discovers the VM images in your cloud account according to the scan scopes specified in `/settings/vm`.
The list of auto-discovered VM images is passed to the scanner for evaluation.
The scanner uses the corresponding `/policies/vulnerability/vms` endpoint to assess each VM image.

### cURL Request

Each VM image scan scope is specified as an element in the endpoint's payload array.

The critical fields for this endpoint are:

* `version` - Cloud provider.
Currently, only Amazon AWS is supported.
* `region` - Region to scan.
* `credentialID` - Credential ID from the credentials store so Prisma Cloud can authenticate with the cloud provider to access the VM images.
* `collections` - Filter for refining the scope of VM images to scan.
You can scope by VM image name and AWS tag.
* `consoleAddr` - Address for Console that Defender (the scanner) can reach over the network to publish scan results.

Refer to the following example cURL command that overwrites all current scan scopes with single scan scope:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/settings/vm' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
  '[
      {
        "version":"aws",
        "region":"us-east-1",
        "credentialID":"IAM Role",
        "collections":[{"name":"All"}],
        "cap": 5,
        "scanners": 1,
        "consoleAddr":"127.0.0.1"
      }
    ]'
```

**Note:** No response will be returned upon successful execution.
