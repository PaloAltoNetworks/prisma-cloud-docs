Returns the status of a regular registry scan that might include the following information:
- Scan is completed: `"completed": true`
- Scan is ongoing.
- Errors: 10 most recent aggregated errors that occured during the scan with error messages such as:
  - "Failed to retrieve repositories info..."
  - "Failed to query image details..."
  - "No available Defender was found"

To view the more details about the progress of a regular or on-demand registry scan, use the `/registry/progress` API endpoint.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/statuses/registry
```
### Response

```json
{
  "scanTime": "2019-07-31T19:42:49.036311567Z",
  "completed": true
}
```