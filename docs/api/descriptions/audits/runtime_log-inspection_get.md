Retrieves all audit events for log inspection checks that are configured under host runtime rules.

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/audits/runtime/log-inspection"
```

### cURL Response

```
{
   "_id": "637639e2b962a7ae744851bf",
   "logfile": "/var/lib/twistlock/log/console.log",
   "line": "DEBU 2022-11-17T13:40:50.066 route_handler_middleware.go:507 GET /api/v1/audits/runtime/log-inspection?limit=20&offset=0&project=Central+Console&reverse=false&search=panic ssugandh admin 0.10s",
   "time": "2022-11-17T13:40:50.067Z",
   "hostname": "jen-cen8-cons-dock-0811t160649-cons-ssugandh-lngcon230.c.twistlock-test-247119.internal",
   "ruleName": "panic_error_log",
   "accountID": "twistlock-test-247119",
   "collections": [
     "All",
     "registry_scan_container_cen8-container_22_11_384_piu",
     "cnnf_cen8_client_itu"
   ],
   "cluster": ""
}

```