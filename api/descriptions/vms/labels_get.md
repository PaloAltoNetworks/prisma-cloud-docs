Returns an array of strings containing all AWS tags of the scanned VM images.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/vms/labels"
```
### cURL Response

Refer to the following example response:

```
[
  "gcp:vmscan",
  "with_pulled_images:true",
  "test-linux-key-2:test-linux-value-2",
  "test-linux-key-1:test-linux-value-1",
  "Name:user-test-b"
]

```