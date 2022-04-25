Retrieves the list of [alert labels](https://docs.twistlock.com/docs/latest/audit/annotate_audits.html) configured in Console.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/settings/custom-labels
```
