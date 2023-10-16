Returns the container audit events data in CSV format when a runtime sensor such as process, network, file system, or system call detects an activity that deviates from the predictive model. 

**Note**: In Console, you can view the same under **Monitor > Events > Container Audits**.

### cURL Request
Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  -o <runtime_container_audits.csv> \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/container/download"
  
```