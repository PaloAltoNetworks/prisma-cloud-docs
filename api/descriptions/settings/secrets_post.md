This endpoint will updates your secret store settings found in the console under **Manage > Authentication > Secrets**.

Please note the data structure returned from endpoint /settings/secrets GET to set in POST

The following example curl command adds a CyberArk secret store to the console with the appID set to `Prisma Cloud Compute_Console` and the URL set to `https://services-myca.twistlock.com:10882`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
  "secretsStores": [
    {
      "name": "Cyberark",
      "type": "cyberark",
      "appID": "Prisma Cloud Compute_Console",
      "url": "https://services-myca.twistlock.com:10882",
      "caCert": {
        "encrypted": ""
      },
      "clientCert": {
        "encrypted": ""
      },
      "useAWSRole": false,
      "region": "",
      "credentialId": "",
      "roleArn": ""
    }
  ]}' \
  https://<CONSOLE>:8083/api/v1/settings/secrets
```
