Configures the logging settings.
This includes Syslog, Stdout, and Prometheus instrumentation.

For more information, see [Logging](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/audit/logging).

## cURL Request

Refer to the following example cURL request that enables verbose scan output for syslog and stdout:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
 -d \
'{
   "syslog": {
     "enabled": true,
     "verboseScan": true,
     "allProcEvents": false,
     "addr": ""
     },
   "stdout": {
     "enabled": true,
     "verboseScan": true,
     "allProcEvents": false,
     }   
}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/logging"
```
