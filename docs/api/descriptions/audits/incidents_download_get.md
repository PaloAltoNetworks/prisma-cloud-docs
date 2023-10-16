Downloads a list of incidents which are not acknowledged (i.e., not in archived state) in CSV format.
Prisma Cloud Compute analyzes individual audits and correlates them together to surface unfolding attacks.
These chains of related audits are called incidents. 

This endpoint maps to the **CSV** hyperlink in **Monitor > Runtime > Incident explorer** in the Console UI.

### cURL Request

The following cURL command downloads all incidents and saves the result in a CSV file called `incidents.csv`:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET \
  -o incidents.csv \
  https://<CONSOLE>/api/v<VERSION>/audits/incidents/download
```

A successful response displays the status of the download.
