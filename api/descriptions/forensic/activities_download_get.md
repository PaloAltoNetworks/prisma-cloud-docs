Downloads all host activities that can be found on *Monitor > Events > Host Activities*

Use the query parameters to filter what data is returned.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o host_activities.csv
  https://<CONSOLE>:8083/api/v1/forensic/activities/download
```
