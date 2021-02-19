This endpoint will return the full metadata of PCF blobstore from page **Monitor > Vulnerabilities > PCF** within the Console.

The following example curl command will retrieve this:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/pcf-droplets?cloudControllerAddresses={cloudControllerAddresses}&id={id}"
```
