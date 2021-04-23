Retrieves a list of all group names as an array of strings.

This endpoint maps to the table data on the **Defend > Vulnerabilities > Images > Registry settings** Console UI page.

### cURL Request

The following cURL command retrieves all the system groups.

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H 'Content-Type: application/json' \
  https://<CONSOLE>/api/v1/groups/names \
```

A sample output would look similar to this:

```json
[
    "admins",
    "secops",
    "devops",
    ""
]
```
