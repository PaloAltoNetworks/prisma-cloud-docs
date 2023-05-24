Adds or deletes Subject Alternative Name(s) (SANs) in Prisma Cloud Compute's certificate.
Defenders use these names to connect to Prisma Cloud Compute.

SANs are set in a single shot.
You should first retrieve the list of SANs with the GET method.
Then add or remove entries from the `consoleSAN` array, and post the updated JSON object.

For more information, see [Certificates](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/configure/certificates).

## cURL Request

Refer to the following example cURL request that uses basic auth to add `node-01.example.com` to the `subjectAltName` field in the certificate:

```bash
curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -w "\nResponse code: %{http_code}\n" \
  -X POST \
  -d '
  {
    "consoleSAN": [
      "10.240.0.34",
      "172.17.0.1",
      "ian-23.c.cto-sandbox.internal",
      "127.0.0.1",
      "node-01.example.com"
    ]
  }' \
  "https://<CONSOLE>/api/v<VERSION>/settings/certs"
```
