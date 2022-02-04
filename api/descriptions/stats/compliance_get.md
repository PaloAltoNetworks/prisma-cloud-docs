Returns compliance statistics, including:

* Compliance rate by regulation, CIS benchmark, and policy rule.
* Trend of failed compliance checks over time.
* List of all compliance checks with their corresponding compliance rate.

This endpoint maps to the table in **Monitor > Compliance > Compliance explorer** in the Console UI.

### cURL Request

Refer to the following example cURL command that retrieves compliance statistics:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/stats/compliance'
```

A successful response returns a summary count of compliance issues. 
The response also shows a detailed list of compliance issues for each running container and host.
