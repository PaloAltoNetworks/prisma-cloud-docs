Downloads all host scan reports in CSV format.

This endpoint maps to the CSV hyperlink in **Monitor > Vulnerabilities > Hosts > Running hosts** in the Console UI.

Refer to the following available options for the `fields` query parameters:
* type
* hostname
* collections
* firewallProtection
* agentless
* stopped
* scanID
* err
* labels
* externalLabels
* clusters
* cloudMetadata
* ecsClusterName
* k8sClusterName
* vulnerabilityRiskScore
* complianceIssuesCount
* complianceDistribution
* vulnerabilityDistribution
* vulnerabilitiesCount
* osDistro
* distro
* osDistroRelease

### cURL Request

Refer to the following example cURL command that downloads all host scan reports to a CSV file called `hosts_report.csv`:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: text/csv' \
  -X GET -o hosts_report.csv \
  https://<CONSOLE>/api/v<VERSION>/hosts/download
```

A successful response displays the status of the download.
