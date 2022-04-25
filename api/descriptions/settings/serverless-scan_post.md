Adds serverless function providers to scan for vulnerabilities.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > Vulnerabilities > Functions > Functions**.
2. Under the **Function scope** table, add a registry item using **+ Add scope**

	**Note:** If the table is not present, use the **Add the first item** link.

3. Click the **Save** button.


### General Set up and Scan Process

This endpoint works hand-in-hand with the `/policies` endpoints.

**To set up a scope for serverless scanning:**

1. Add your scope information using this endpoint.

   For example, specify a region and credentials for accessing the AWS account.

2. Prisma Cloud auto-discovers the serverless functions in scope.

3. The list of auto-discovered serverless functions is passed to the scanner for evaluation.
  
   The scanner uses the corresponding `/policies/vulnerability/serverless` endpoint to assess each serverless function.

### cURL Request

Each scan scope is specified as an element in array.

The critical fields for this endpoint are:

* `provider` - Host provider name. For example, `aws` refers to Amazon Web Services.
* `credentialID` - ID of the credentials in the credentials store to authenticate against the service provider.

Refer to the following example cURL command that adds serverless scan scopes to scan with a new single serverless scan scope.

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/settings/serverless-scan' \
  -k \
  -X POST \
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
