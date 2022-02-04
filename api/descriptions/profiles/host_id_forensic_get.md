Returns the forensic data for a host, which can be used to investigate runtime incidents.


## cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v1/profiles/host/{id}/forensic"
```
