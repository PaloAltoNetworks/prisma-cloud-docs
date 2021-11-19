Enables or disables the [Projects](https://docs.twistlock.com/docs/latest/deployment_patterns/projects.html) feature.
Projects are enabled when an instance of Console is designated as master.

The following example curl command designates `<CONSOLE>` as master.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "master":true
 }' \
  https://<CONSOLE>:8083/api/v1/settings/projects
```
