Retrieves all host scan reports. 

This endpoint maps to the **Running hosts** table in **Monitor > Vulnerabilities > Hosts > Running hosts** in the Console UI.

### cURL Request

Refer to the following cURL command that retrieves all host scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/hosts
```

A successful response returns all host scan reports.
