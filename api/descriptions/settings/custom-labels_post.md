Adds [alert labels](https://docs.twistlock.com/docs/latest/audit/annotate_audits.html) to the system.

### cURL Request

Refer to the following example cURL command that designates the labels `first` and `second` as alert labels:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"labels": ["first","second"]}' \
  https://<CONSOLE>/api/v1/settings/custom-labels
```
