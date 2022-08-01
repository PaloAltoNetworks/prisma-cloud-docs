Retrieves a list of incidents that are not acknowledged (i.e., not in archived state).
Prisma Cloud Compute analyzes individual audits and correlates them together to surface unfolding attacks.
These chains of related audits are called incidents. 

This endpoint maps to the table in **Monitor > Runtime > Incident explorer** in the Console UI.

### cURL Request

Refer to the following example cURL command that retrieves a list of unacknowledged incidents (not in the archived state):

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/incidents?acknowledged=false"
```

A successful response returns the incidents.
