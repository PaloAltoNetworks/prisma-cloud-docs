Creates an augumented dockerfile with RASP defender and dependencides included as a zip file.]

For more information about how to use this endpoint, see
[Deploy a Defender RASP using the API](https://docs.twistlock.com/docs/19.07/install/install_defender/install_rasp_defender.html#embed-rasp-defender).

The following example curl command returns a RASP Defender zip file.
The `<HOSTNAME>` query parameter specifies the address that Defender uses to communicate with Console.
It can be a DNS name or IP address.

`<HOSTNAME>` is a single list item from the `/api/v1/defenders/names` endpoint.

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  -o rasp-defender.zip
  'https://<CONSOLE>:8083/api/v1/defenders/rasp?appId=<ApplicationID>&consoleaddr=<HOSTNAME>&dataFolder=<FolderName>&dockerfile=<PathToDockerfile>'
```
