Sets the Tanzu Application Service (TAS) settings.

### cURL Request

Refer to the following example cURL command that configures the TAS settings:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/settings/tas'
  -k \
  -X POST \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
  '[
      {
        "cap": 5,
        "cloudControllerAddress": "https://example.com",
        "hostname": "vm-host",
        "pattern": "droplet-name"
      }
    ]'
```