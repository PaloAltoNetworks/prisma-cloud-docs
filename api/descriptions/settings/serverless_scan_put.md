Updates the serverless scan scopes.
All scan scopes are updated in a single shot.

### cURL Request

Each scan scope is specified as an element in array.

The critical fields for this endpoint are:

* `provider` - Host provider name. For example, `aws` refers to Amazon Web Services.
* `credentialID` - ID of the credentials in the credentials store to authenticate against the service provider.

Refer to the following example cURL command that overwrites all serverless scan scopes to scan with a new single serverless scan scope:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/settings/serverless-scan' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
  '[
      {
        "provider": "aws",
        "credential":{},
        "credentialID":"IAM Role"  
      }
    ]'
```

**Note:** No response will be returned upon successful execution.