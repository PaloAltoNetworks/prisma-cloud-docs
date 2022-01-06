Downloads the twistcli binary executable for MacOS platforms.

This endpoint maps to the **MacOS platform** hyperlink in **Manage > System > Utilities** in the Console UI.

### cURL Request

The following cURL command downloads the twistcli binary executable for MacOS platforms.

```bash
$ curl -k \
  -u <USER> \
  -L \
  -o twistcli \
  https://<CONSOLE>/api/v1/util/osx/twistcli
```

A successful response displays the status of the download.
