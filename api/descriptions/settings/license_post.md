Configures the Prisma Cloud Compute license.
Use this endpoint, along with `/api/v1/signup`, as part of the initial set up flow after Prisma Cloud Compute is first installed.

For more information, see [Licensing](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/welcome/licensing).

## cURL Request

Refer to the following example cURL request that uses basic auth to set your license:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"key": "<LICENSE_KEY>"}' \
  https://<CONSOLE>/api/v<VERSION>/settings/license
```
