Downloads the twistcli binary executable for MacOS platforms based on ARM64 architecture.

**Note:** This endpoint maps to the **MacOS platform** hyperlink in **Manage > System > Utilities** in the Console UI.

### cURL Request

Refer to the following example cURL command that downloads and saves the “twistcli” binary executable for ARM64 bit MacOS platforms to your HOME directory:

```bash
$ curl -k \
 -u <USER> \
 -H 'Content-Type: application/json' \
 -X GET -o <FILE NAME> \
 'https://<CONSOLE>/api/v<VERSION>/util/osx/arm64/twistcli'                                                               
```

A successful response displays the status of the download.