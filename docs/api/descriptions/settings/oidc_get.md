Returns the OpenID Connect configuration settings.

## cURL Request

Refer to the following example cURL request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/oidc"
```

## cURL Response

Refer to the following example cURL response:

```bash
$ {
 "enabled": true,
 "clientID": "0oajdm6atavfYyJfr4x6",
 "clientSecret": {
   "encrypted": "rnEk+1be20FLv+BYnDX4s5/T0NOb49hkNkaZQtgiF7K2s65"
 },
 "providerName": "",
 "authURL": "",
 "tokenURL": "",
 "groupScope": "groups",
 "groupClaim": "groups",
 "userClaim": "",
 "cert": "",
 "openshiftBaseURL": "",
 "openIDIssuesURL": "https://ss-123456.okta.com",
 "providerAlias": "oidc_okta_ss"
}
```
