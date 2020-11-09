Downloads a script that installs a client certificate, client private key, and certificate authority certificate for the authenticated user.

The following example curl command uses basic auth to download and run the install script for your client certs:

```bash
$ curl -k \
  -u <USER> \
  -X GET \
  https://<CONSOLE>:8083/api/v1/certs/client-certs.sh | sh
```
