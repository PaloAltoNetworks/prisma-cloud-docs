Retrieves all host Web-Application and API Security (WAAS) audit events.

**Note:** These are based on violations of WAAS policies defined under **Defend > WAAS > Host > Host WAAS Policy**.

Use the following mandatory query parameters to fetch results:
* **from**: Specifies the start time in UTC standard of the time period for which the audit events are returned.
* **to**: Specifies the end time in UTC standard of the time period for which the audit events are returned.
* **buckets**: Specifies the number of buckets (buckets of audits based on aggregation logic) to return. Values in the range  1-100 are accepted.

### cURL Request

Refer to the following example cURL command that retrieves host WAAS audit events for a specific time frame:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/firewall/app/hosttimeslice?from=2022-11-15T15:23:57Z&to=2022-11-16T15:23:57Z&buckets=5"
```

### cURL Response

```
{
    "start": "2022-11-16T10:35:57Z",
    "end": "2022-11-16T15:23:57Z",
    "count": 46
}

```
**Response Parameters**:
* **start**: Specifies the start time of the bucket in date-time UTC format.
* **end**: Specifies the end time of the bucket in date-time UTC format.
* **count**: Specifies the number of audit occurrences.
