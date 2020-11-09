This endpoint will return the cloud contoller addresses configured for PCF Blobstore scanning.

You can also add optional query paramaters to this api call, in this example `cloudControllerAddresses` and/or `id`

The following example curl command retrieves the list of addresses:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>:8083/api/v1/pcf-droplets/addresses?cloudControllerAddresses={cloudControllerAddresses}&id={id}"
```
