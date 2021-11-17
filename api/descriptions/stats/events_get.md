Returns events statistics for your environment.

The following example command that uses curl and basic auth to retrieve daily stats:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/events
```

Here is an example of what would be returned:


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

