Returns events statistics for your environment.

### cURL Request

Refer to the following example cURL command retrieves event stats:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/stats/events
```

### Response


```json
{
  "containerAppFirewall": 0,
  "hostAppFirewall": 0,
  "containerRuntime": 0,
  "containerNetworkFirewall": 0,
  "hostRuntime": 0,
  "hostNetworkFirewall": 0,
  "hostActivities": 0,
  "raspAppFirewall": 0,
  "raspRuntime": 0,
  "serverlessRuntime": 0,
  "logInspection": 0,
  "fileIntegrity": 0,
  "dockerAccess": 0,
  "kubernetesAudits": 0,
  "trustAudits": 0
}
```

