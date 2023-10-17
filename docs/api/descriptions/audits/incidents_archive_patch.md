Acknowledges an incident and moves it to an archived state. 
Requires a path parameter: id, an Incident ID

You can get an incident ID from the list of incidents using the endpoint GET /api/vVERSION/audits/incidents.

### cURL Request
Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PATCH \
  -d {"acknowledged":true} \
  "https://<CONSOLE>/api/v<VERSION>/audits/incidents/acknowledge/637627beb2a8e98a1c36a9db"

```
To  undo this action (unarchive an incident), set the body parameter "acknowledged": false