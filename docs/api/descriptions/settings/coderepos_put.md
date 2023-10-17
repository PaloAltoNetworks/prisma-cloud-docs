Updates the code repositories to scan.
The list of code repositories to scan is updated in a single shot.

To invoke this endpoint in the Console UI:

1. Navigate to **Defend > Vulnerabilities > Code repositories**.
2. Under the **GitHub repositories scan scope** table, add a scope item using **+ Add scope**
  
   **Note:** If your table is not present add an item to the table by clicking **Add the first item**.

3. Click the **Save** button.

### General Set up and Scan Process

This endpoint works hand-in-hand with the `/policies` endpoints.

**To set up Prisma Cloud to scan your code repositories:**

1. Add a scan scope with this endpoint (`/settings/coderepos`), where the principle component is the account information for the service that hosts your code repositories.

   For example, specify the the credentials of your GitHub account.
   You can further refine the scope by specifying which repos to scan using explicit strings or pattern matching.
   Scan all repos by specifying a wildcard.

2. Prisma Cloud auto-discovers all code repositories in each scan scope.

   The system invokes the GET `/coderepos/discover` endpoint to discover the available repositories using the credential ID provided.

3. The list of auto-discovered code repositories is passed to the scanner for evaluation.
  
   The scanner uses the corresponding `/policies/vulnerability/coderepos` endpoint to assess each code repository.

### cURL Request

Each scan scope is specified as an element in the endpoint's payload array.
Itemize the repositories to scan in the `repositories` array.
A wildcard tells Prisma Cloud to scan all repos in the account.

The critical fields for this endpoint are:

* `type` - Hosting service, such as GitHub (`github`)
* `credentialID` - Credential, from the credentials store, that Prisma Cloud uses to authenticate with the hosting service.
* `repositories` - List of repository names.
The format is `<owner>/<repo_name>`.

Refer to the following example cURL command that overwrites all code repository scan scopes with a single new scan scope:

```bash
$ curl 'https://<CONSOLE>/api/v<VERSION>/settings/coderepos' \
  -k \
  -X PUT \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -d \
'[
   {
      "type":"github",
      "publicOnly":false,
      "credentialID":"<CREDENTIAL_ID>",
      "repositories":[
         "*"
      ]
   }
]'
```
This scan scope includes all repositories in the GitHub account that can be accessed with `CREDENTIAL_ID`.

**Note:** No response will be returned upon successful execution.
