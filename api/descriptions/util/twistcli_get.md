Downloads the twistcli binary executable for Linux platforms.

This endpoint maps to the **Linux platform** hyperlink in **Manage > System > Utilities** in the Console UI.

### cURL Request

The following cURL command downloads the twistcli binary executable for Linux platforms.

```bash
$ curl -k \
  -u <USER> \
  -L \
  -o twistcli \
  https://<CONSOLE>/api/v1/util/twistcli
```

A successful response displays the status of the download.
