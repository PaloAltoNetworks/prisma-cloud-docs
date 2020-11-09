Configures the forensics system.

The following example curl command allocates 100 MB of local disk space for container forensic data and 10 MB for host forensics data.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "enabled": true,
   "containerDiskUsageMb": 100,
   "hostDiskUsageMb": 10   
}' \
  https://<CONSOLE>:8083/api/v1/settings/forensic
```
