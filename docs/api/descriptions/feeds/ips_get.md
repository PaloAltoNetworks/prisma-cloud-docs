Retrieves the customized list of block-listed suspicious or high-risk IP addresses.

### cURL Request

The following cURL command retrieves the list of globally block-listed suspicious or high-risk IP addresses.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/feeds/custom/ips
```

### Response

A successful response will return a list of suspicious or high-risk IP addresses that will be banned.

```json
{
	"_id":"<ID>",
	"modified":"2020-11:00:00T00:00:01.62Z",
	"feed":["193.171.1.1","193.171.1.2"]},
	"digest":"<DIGEST>"
}
```
