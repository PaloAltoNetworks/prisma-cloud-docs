Sets up your Prisma Cloud Compute license.
Use this endpoint, along with `/api/v1/signup`, as part of the initial set up flow after Prisma Cloud Compute is first installed.

Although this endpoint is supported, no backwards compatibility is offered for it.

The following example curl command uses basic auth to set your license.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"key": "<LICENSE_KEY>"}' \
  https://<CONSOLE>:8083/api/v1/settings/license
```
