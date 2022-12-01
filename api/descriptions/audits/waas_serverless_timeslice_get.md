Retrieves all serverless Web-Application and API Security (WAAS) audit buckets based on a specified query time frame in UTC.

**Note:** These are based on violations of WAAS policies defined under **Defend > WAAS > Serverless > Serverless WAAS Policy**.

Use the following mandatory query parameters to fetch results:
* **from**: Specifies the start time in UTC standard of the time period for which the audit events are returned.
* **to**: Specifies the end time in UTC standard of the time period for which the audit events are returned.
* **buckets**: Specifies the number of buckets (buckets of audits based on aggregation logic) to return. Values in the range  1-100 are accepted.

### cURL Request

Refer to the following example cURL command that retrieves the serverless WAAS audit events for a :

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/serverless/timeslice?from=2022-11-15T15:23:57Z&to=2022-11-16T15:23:57Z&buckets=5"
```

### cURL Response

```
{
        "start": "2022-11-21T04:26:58.066Z",
        "end": "2022-11-22T02:49:58.549Z",
        "count": 1
}

```
**Response Parameters**:
* **start**: Specifies the start time of the bucket in date-time UTC format.
* **end**: Specifies the start time of the bucket in date-time UTC format.
* **count**: Specifies the number of audit occurrences.
