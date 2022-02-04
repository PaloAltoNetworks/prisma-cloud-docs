Retrieves Tanzu Application Service (TAS) settings.

### cURL Request

Refer to the following example cURL command that retrieves all TAS settings:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/tas"
```