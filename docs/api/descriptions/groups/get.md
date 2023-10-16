Retrieves the list of all groups.

This endpoint maps to the table data on the **Manage > Authentication > Groups** Console UI page.

### cURL Request

Refer to the following example cURL command that retrieves all the system groups.

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H 'Content-Type: application/json' \
  https://<CONSOLE>/api/v<VERSION>/groups
```
