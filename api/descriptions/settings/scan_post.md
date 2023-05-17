Configures the Prisma Cloud Compute scanner settings.

For more information, see [Configure Scanning](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/configure/configure_scan_intervals).
## cURL Request

Refer to the following example cURL request that configures the following scan intervals:

* Scan registries and serverless functions once per week.
* Scan images, containers, and hosts once per day.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "imagesScanPeriodMs":86400000,
   "containersScanPeriodMs": 86400000,
   "systemScanPeriodMs": 86400000,
   "serverlessScanPeriodMs": 604800000,
   "registryScanPeriodMs":604800000
}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/scan"
```
