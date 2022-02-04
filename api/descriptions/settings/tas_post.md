Sets the Tanzu Application Service (TAS) settings.

### cURL Request

Refer to the following example cURL command that configures the TAS settings:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "cap": 5,
   "cloudControllerAddress": "https://example.com",
   "hostname": "vm-host"
   "pattern": "droplet-name" 
 }' \
  "https://<CONSOLE>/api/v<VERSION>/settings/tas"