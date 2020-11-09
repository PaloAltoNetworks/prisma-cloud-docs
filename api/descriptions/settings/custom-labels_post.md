Adds [alert labels](https://docs.twistlock.com/docs/latest/audit/annotate_audits.html) to the system.
The following example designates the labels `first` and `second` as alert labels.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"labels": ["first","second"]}' \
  https://<CONSOLE>:8083/api/v1/settings/custom-labels
```
