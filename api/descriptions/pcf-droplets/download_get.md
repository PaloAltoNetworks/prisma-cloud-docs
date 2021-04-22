This endpoint will download the list of configured cloud controller addresses configured for PCF Blobstore scanning.

The following example curl command retrieves the list of addresses and outputs it to a file call `PCF_blobstores.csv`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o PCF_blobstores.csv
  "https://<CONSOLE>:8083/api/v1/pcf-droplets/download?cloudControllerAddresses={cloudControllerAddresses}&id={id}"
```

