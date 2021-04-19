This endpoint retrieves a list of incidents which are not acknowledged (i.e., not in archived state).
Twistlock analyzes individual audits and correlates them together to surface unfolding attacks.
These chains of related audits are called incidents. 

This endpoint maps to the table in **Monitor > Runtime > Incident explorer** in the Console UI.

### cURL Request

The following cURL command retrieves all incidents.

```bash
$ curl -k \
  -u <USER> \
  https://<CONSOLE>/api/v1/audits/incidents
```

A successful response returns the incidents.
