Retrieves all host scan reports.

> _**Note:**_ The API rate limit for this endpoint is 30 requests per minute.
You'll see an HTTP error response 429 if the limit exceeds.

This endpoint maps to the **Running hosts** table in **Monitor > Vulnerabilities > Hosts > Running hosts** in the Console UI.

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
* k8sClusterAddr
* vulnerabilityRiskScore
* complianceIssuesCount
* complianceRiskScore
* complianceDistribution
* vulnerabilityDistribution
* vulnerabilitiesCount
* osDistro
* distro
* osDistroRelease

### cURL Request

Refer to the following cURL command that retrieves all host scan reports:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/hosts
```

A successful response returns all host scan reports.
