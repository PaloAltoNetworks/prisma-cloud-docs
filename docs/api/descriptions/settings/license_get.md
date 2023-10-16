Returns the details about the installed license.

## cURL Request

Refer to the following example cURL request that retrieves the license details.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/license"
```
