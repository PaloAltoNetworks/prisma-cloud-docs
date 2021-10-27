Configures the Prisma Cloud Compute scanner.

The following example curl command configures the following scan intervals:

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
  https://<CONSOLE>:8083/api/v1/settings/scan
```
