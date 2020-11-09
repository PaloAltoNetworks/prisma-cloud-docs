This endpoint will allow for updating settings for PCF (Pivotal Cloud Foundry) Blobstore scanning. 

The following example curl command uses basic auth to set up a PCF Blobstore scanner that scans the last `5` droplets for every droplet in the PCF Blobstore:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"cap":"5","cloudControllerAddress":"https://my-cloud-controller.twistlock.com","pattern":"*"}' \
  https://<CONSOLE>:8083/api/v1/settings/pcf
```

