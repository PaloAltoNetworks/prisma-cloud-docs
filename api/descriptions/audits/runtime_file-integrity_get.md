Twistlock can provide audits for file-integrity checks that are configured under host runtime rules.

The following example uses basic auth to list these audits:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/runtime/file-integrity
```

