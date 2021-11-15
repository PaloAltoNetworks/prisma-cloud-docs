Returns the workload statistics from Console.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/stats/workload
```

Here is an example of when would be returned:

```json
{
  "Timestamp": "0001-01-01T00:00:00Z",
  "HourSamples": 0,
  "HourAvg": 0,
  "DailySamples": null,
  "exceeded": false,
  "avg": 0,
  "msg": ""
}
```
