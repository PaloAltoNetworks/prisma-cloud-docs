Downloads the twistcli binary executable for Linux platforms.

This endpoint maps to the **Linux platform** hyperlink in **Manage > System > Utilities** in the Console UI.

### cURL Request

Refer to the following example cURL command that downloads and saves the “twistcli” binary executable to your HOME directory:

```bash
$ curl -k \
	-u <USER> \
	-X GET -o <FILE NAME> \
'https://<CONSOLE>/api/v<VERSION>/util/twistcli'                                                               
```

A successful response displays the status of the download.
