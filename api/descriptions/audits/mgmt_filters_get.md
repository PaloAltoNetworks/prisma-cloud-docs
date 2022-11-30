Retrieves a list of management audit types from your environment. 
Use these filters to query management audit events.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/mgmt/filters"
```
### cURL Response

```
{
 "type": [
   "group",
   "login",
   "role",
   "rule",
   "settings",
   "user"
 ],
 "username": [
   "admin2",
   "ReadOnly",
   "admin",
   "ci",
   "development-user"
 ]
}

```