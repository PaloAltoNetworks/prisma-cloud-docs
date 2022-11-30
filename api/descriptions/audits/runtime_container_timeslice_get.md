Retrieves the container audit events when a runtime sensor such as process, network, file system, or system call detects an activity that deviates from the predictive model for a specific time frame.

**Note**: In Console, you can view the same under **Monitor > Events > Container Audits**.

Use the following mandatory query parameters to fetch results:
* **from**: Specifies the start time in UTC standard of the time period for which the audit events are returned.
* **to**: Specifies the end time in UTC standard of the time period for which the audit events are returned.
* **buckets**: Specifies the number of buckets (buckets of audits based on aggregation logic) to return. Query within the range of 1-100.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/container/timeslice?from=2022-11-15T15:23:57Z&to=2022-11-16T15:23:57Z&buckets=5"
```
### cURL Response

```
{
   "start": "2022-11-16T10:35:57Z",
   "end": "2022-11-16T15:23:57Z",
   "count": 87
}

```

**Response Parameters**:
* **start**: Specifies the start time of the bucket in date-time UTC format.
* **end**: Specifies the end time of the bucket in date-time UTC format.
* **count**: Specifies the number of audit occurrences.