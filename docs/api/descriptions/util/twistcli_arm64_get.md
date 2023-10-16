Downloads the twistcli binary executable for ARM64 bit Linux platforms.

This endpoint maps to the **Linux platform** hyperlink in **Manage > System > Utilities** in the Console UI.

### cURL Request

Refer to the following example cURL command that downloads and saves the “twistcli” binary executable to your HOME directory:

```bash
$ curl -k \
 -u <USER> \
 -H 'Content-Type: application/json' \
 -X GET -o <FILE NAME> \
 'https://<CONSOLE>/api/v<VERSION>/util/arm64/twistcli'                                                               
```

A successful response displays the status of the download.