Triggers a new scan for all images when a new image is added to the registry or a new scan for an individual image.
 
Consider the following points for a regular scan:
 
* You cannot make multiple parallel scan requests with a regular scan.
* You either need to stop the on-going scan using the `api/vVERSION/registry/stop` or wait for the on-going scan to finish.
For information on stopping a regular scan, see [Stop Registry Scan](https://prisma.pan.dev/api/cloud/cwpp/registry#operation/post-registry-stop)
* You can view the scan result or response for all the images by using the `api/vVERSION/registry` API endpoint.
For information on scan result, see [Get Registry Scan Report](https://prisma.pan.dev/api/cloud/cwpp/registry#operation/get-registry)
 
### cURL Request
Refer to the following example cURL command that forces Prisma Cloud Compute to rescan all registry images:
 
```bash
$ curl -k \
 -u <USER> \
 -H 'Content-Type: application/json' \
 -X POST \
 https://<CONSOLE>/api/v<VERSION>/registry/scan
```
 
Refer to the following example cURL command that forces Prisma Cloud Compute to re-scan a specific image:
 
```bash
$ curl -k \
 -u <USER> \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{"tag":{"registry":"<REGISTRY>","repo":"<REPO>","tag":"<TAG>","digest":""}}'\
 https://<CONSOLE>/api/v<VERSION>/registry/scan
```
