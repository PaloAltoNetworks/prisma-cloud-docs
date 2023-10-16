Update an existing alert profile created in the system.

The following example curl command uses basic auth to add a Jira Alert profile:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  https://<CONSOLE>:8083/api/v1/alert-profiles \
  -d '  {
    "name": "jira",
    "_id": "jira",
    "jira": {
      "enabled": true,
      "projectKey": "TWIS",
      "issueType": "Task",
      "priority": "High",
      "labels": [],
      "assignee": ""
    }
    "policy": {
      "cve": {
        "enabled": true,
        "allRules": true,
        "rules": [],
        "clients": [
          "jira"
        ]
      }
    } '
```
