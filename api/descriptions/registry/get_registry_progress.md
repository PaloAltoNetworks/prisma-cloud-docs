Shows the progress of an ongoing regular or on-demand scan on hosts.

### cURL Request

Refer to the following example cURL command:

```
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  “https://<CONSOLE>/api/v<VERSION>/registry/progress”
```

### cURL Response

Refer to the following example cURL response:

```
{
    "hostname": "",
    "id": "",
    "scanTime": "2022-11-09T11:10:51.649Z",
    "type": "agentlessHost",
    "discovery": true,
    "total": 5,
    "scanned": 2,
    "title": "Agentless discovering"
  }
]
```