Downloads a free IP to Country Lite database file in MMDB format.

### cURL Request

Refer to the following example cURL command that fetches an MMDB file:

```bash
curl -k \
	-u <USER> \
	-X GET -o <FILE NAME> \
'https://<CONSOLE>/api/v<VERSION>/util/dbip-countrylite.mmdb'                                                               
```                                                               
A successful response displays the status of the download.
