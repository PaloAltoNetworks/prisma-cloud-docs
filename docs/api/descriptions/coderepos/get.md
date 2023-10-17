Retrieves all code repository scan reports.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per 30 seconds.
You get an HTTP error response 429 if the limit exceeds.

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
