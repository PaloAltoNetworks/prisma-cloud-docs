Returns a list of static compliance and vulnerability data.  This data can be used in building out reports with the API.  This data can be correlated with the endpoint */images* specifically *complianceVulnerabilities* and *cveVulnerabilities* within, to more thoroughly generate the reports.



```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/static/vulnerabilities
```

