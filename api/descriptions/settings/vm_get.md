Retrieves the list of VM image scan scopes.

This endpoint maps to the **VM images scope** table data in the **Defend > Vulnerabilities > Hosts > VM images** Console UI.

### cURL Request

The following cURL command retrieves all the scopes used for pattern matching on VM functions.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v1/settings/vm'
```
