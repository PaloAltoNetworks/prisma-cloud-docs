Configure your logging settings. This includes Syslog, Stdout, and Prometheus instrumentation.

The following example curl command enables verbose scan output for syslog and stdout.

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
  https://<CONSOLE>:8083/api/v1/settings/logging
```
