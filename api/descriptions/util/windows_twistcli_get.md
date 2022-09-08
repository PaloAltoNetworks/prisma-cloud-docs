Downloads the twistcli binary executable for Windows platforms.

This endpoint maps to the **Windows platform** hyperlink in **Manage > System > Utilities** in the Console UI.

### cURL Request

The following cURL command downloads the twistcli binary executable for Windows platforms.

```bash
$ curl -k \
  -u <USER> \
  -L \
  -o twistcli.exe \
  https://<CONSOLE>/api/v1/util/windows/twistcli.exe
```

A successful response displays the status of the download.
