Retrieves all VM image scan reports.

This endpoint maps to the table in **Monitor > Vulnerabilities > Hosts > VM images** in the Console UI.

### cURL Request

The following cURL command retrieves all VM image scan reports.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/vms \
```

A successful response returns the scan reports.
