This endpoint will return settings for PCF (Pivotal Cloud Foundry)Blobstore scanning, which can be found in the console under **Defend > Vulnerabilities > PCF Blobstore**. This requires that you have a defender configured for PCF Blobstore scanning. For more information, see [PCF blobstore scanning](https://docs.twistlock.com/docs/latest/vulnerability_management/pcf_blobstore.html).

The following example curl command uses basic auth to retrieve the current PCF Blobstore scanning settings:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/settings/pcf
```
