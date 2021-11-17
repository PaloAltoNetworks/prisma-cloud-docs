Returns a summary count of the CVEs in the images, containers, hosts, and serverless functions of your environment, organized by day (`_id`).

The response also includes detailed descriptions for each CVE currently affecting the resources in your environment at the time of the last scan.

This endpoint maps to the table in **Monitor > Vulnerabilities > Vulnerability explorer > Trend by vulnerabilities** in the Console UI.

### cURL Request

The following cURL command retrieves a summary count of the CVEs and detailed descriptions for each CVE.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/stats/vulnerabilities
```

A successful response returns a summary count of the CVEs and detailed descriptions for each CVE.
