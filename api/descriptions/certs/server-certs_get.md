Retrieves the server certificate bundle from Prisma Cloud Compute that contains a chain of certificates.

* Certificate Authority (CA) certificate in PEM
* RSA Private Key for server in PEM
* Server certificate in PEM
* Defender CA certificate in PEM
* Defender RSA Private Key for client in PEM
* Defender client certificate in PEM

### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -H 'Content-Type: application/json' \
  -u <USER> \
  -X GET \
  "https://<CONSOLE>/api/v1/certs/server-certs.sh"
```
### cURL Response

```
#!/bin/sh
# Copy Certificate Authority
echo -n "-----BEGIN CERTIFICATE-----
MIIDHDCCAgSgAwIBAgIQDBOoX575aweiQ6j6I…hXgEM=
-----END CERTIFICATE-----
" > ca.pem
# Copy Server key
echo -n "-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,a7a8cbceec7e97d51c04ce03f1b4c4dc
HwlxgvmGJw068VUEletmSSBjE54Q+8BGcWuYc…3PjIj2nuD4PTtOULiuLnAoONb0
-----END RSA PRIVATE KEY-----
" > server-key.pem
# Copy Server Cert
echo -n "-----BEGIN CERTIFICATE-----
MIIDOjCCAiKgAwIBAgIRAOCRfG1Sot…5SY03wZf20LvAzrLTRLsIAbsivp0Ljmvt
drBPViPXgryvwhpnaxU=
-----END CERTIFICATE-----
" > server-cert.pem
# Copy the defender certificate authority
echo -n "-----BEGIN CERTIFICATE-----
MIIDHTCCAgWgAwIBAgIRAMAqTE7/cvmwb…xLx9lzxemN
-----END CERTIFICATE-----
" > defender-ca.pem
# Copy the defender client key
echo -n "-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,ab1bca8bc354c0866cfc26fd946c70b5

x1nwAJw5sbjoSL7aUpO3rP8IkMz63X1dD…3k1SVZSph63rRvv6d5O
-----END RSA PRIVATE KEY-----
" > defender-client-key.pem
# Copy the defender client cert
echo -n "-----BEGIN CERTIFICATE-----
MIIDJzCCAg+gAwIBAgIQcb6VdD45Jbla…6kXfxAvSiLTs4mhC1wg68ZSDUQ==
-----END CERTIFICATE-----
" > defender-client-cert.pem

```