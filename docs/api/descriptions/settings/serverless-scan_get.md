Retrieves the list of serverless function scan scopes.
Serverless scan scopes specify a region and a credential.

This endpoint maps to the **Function scope** table data in the **Defend > Vulnerabilities > Functions > Functions** Console UI.

### cURL Request

Refer to the following example cURL command that retrieves a list of serverless scan scopes:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  'https://<CONSOLE>/api/v<VERSION>/settings/serverless-scan'
```

A successful response returns a list of scan scopes.
