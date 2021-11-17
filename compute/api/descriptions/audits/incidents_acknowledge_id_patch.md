Use this call to acknowledge an incident and move it to Archived state. 
Incident ID of the incident you want to archive is required.
You can get incident ID from the list of incidents in `GET /api/v1/audits/incidents`.

Note that you can undo this action by changing "true" to "false" in the following example. 

The following example uses basic auth and PATCH method to acknowledge an incident

```bash
$ curl -k \
  -u <USER> \
   https://aqsa-console:8083/api/v1/audits/incidents/acknowledge/5c76e18784bf4b7278d9a820 -d '{"acknowledged":true}'
```

Where `5c76e18784bf4b7278d9a820` is the incident ID

