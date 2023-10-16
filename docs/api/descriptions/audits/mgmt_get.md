Retrieves a list of all management audit events.

Management audit events are:
* Changes to any settings (including previous and new values)
* Changes to any rules (create, modify, or delete)
* Logon activities (success and failure)

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/mgmt"
```

### cURL Response

```
{
   "username": "user",
   "sourceIP": "10.47.99.218",
   "time": "2022-11-22T03:11:15.39Z",
   "type": "login",
   "diff": "",
   "status": "successful login attempt",
   "failure": false,
   "api": "/api/v1/authenticate"
 }


```
