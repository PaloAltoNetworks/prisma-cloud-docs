Returns a list of static compliance and vulnerability data.
This data can be used for building out reports with the API.
This data can be correlated with the `/api/v1/images` endpoint, specifically the the `complianceVulnerabilities` and `cveVulnerabilities` objects, to generate more thorough reports.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/static/vulnerabilities
```

