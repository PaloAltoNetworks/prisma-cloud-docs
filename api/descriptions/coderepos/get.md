Retrieves all code repository scan reports.

This endpoint maps to the **Code repositories** table in **Monitor > Vulnerabilities > Code repositories** in the Console UI.

### cURL Request

The following cURL command retrieves all code repository scan reports.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/coderepos \
```

A successful response returns all code repository scan reports.
