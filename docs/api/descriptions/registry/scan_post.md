Triggers a new scan for all images when a new image is added to the registry or a new scan for an individual image.
 
You can use the scanning feature in the following ways:
 
## Regular scan
This feature allows you to trigger a new scan immediately for all the images when a new image is added to the registry or trigger a scan for an individual image.
 
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
 
## On-demand scan
This feature allows you to trigger a new scan immediately for an individual image and not wait for the next periodic scan.
 
**Note**: For an on-demand scan, you must pre-define the image registry scope in the registry scanning configuration.
 
Consider the following points for an on-demand scan:
 
* You can trigger multiple on-demand image scans without interrupting the main registry scanning process.
* You cannot stop a running on-demand scan, you can only initiate a new parallel scan.
* You can view the on-demand scan result or response by using query parameter `name` that specifies the full image name in the `api/vVERSION/registry` API endpoint.
For information on scan result, see [Get Registry Scan Report](https://pan.dev/prisma-cloud/api/cwpp/get-registry/)
 
 
### cURL Request
Refer to the following example cURL command to trigger an on-demand scan for an image:
 
```bash
$ curl -k \
 -u <USER> \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{“onDemandScan”:true,“tag”:{“registry” :“<REGISTRY>”,“repo”:“<REPO>”,“digest”:“”}}' \
 "https://<CONSOLE>/api/v<VERSION>/registry/scan"
```
