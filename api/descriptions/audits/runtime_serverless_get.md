Retrieves all scan events for any configured serverless functions in Prisma Cloud Compute.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/serverless" 
```
### cURL Response

```
{
        "time": "2022-11-22T12:27:19.329Z",
        "fqdn": "",
        "type": "",
        "effect": "",
        "ruleName": "",
        "msg": "C:\\home\\xmrig launched by C:\\Windows\\system32\\inetsrv\\w3wp.exe and is identified as a crypto miner. Full command: \"C:\\home\\xmrig\" /I windows C:\\Windows\\*",
        "count": 1,
        "function": "Test44",
        "region": "Central US",
        "runtime": "dotnet",
        "provider": "azure"
}

```