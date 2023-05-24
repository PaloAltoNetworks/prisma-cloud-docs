Creates a custom alert label to augment audit events.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d "{labels:"new_label"}" \
  "https://<CONSOLE>/api/v<VERSION>/settings/custom-labels"
```
