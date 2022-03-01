Although this is a supported endpoint, it’s not versioned. 
For more information about supported and versioned endpoints, see [Stable endpoints](https://prisma.pan.dev/docs/cloud/cwpp/stable-endpoints)

Returns a JSON object of the agentless scan progress.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/agentless/progress
```