Returns the OAuth configuration settings.

## cURL Request

Refer to the following example cURL request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/oauth"
```

## cURL Response

Refer to the following example cURL response:

```bash
{
 "enabled": true,
 "clientID": "ef3a806a249a31b7d15e",
 "clientSecret": {
   "encrypted": "O27GsQ7PDX4LrVx6q+A7sMLUAKTbKU3DAYTZyaOhqTqdNwI7raKFCA3/RrmRPUgk"
 },
 "providerName": "github",
 "authURL": "https://github.com/login/oauth/authorize",
 "tokenURL": "https://github.com/login/oauth/access_token",
 "groupScope": "",
 "groupClaim": "",
 "userClaim": "",
 "cert": "",
 "openshiftBaseURL": "",
 "openIDIssuesURL": "",
 "providerAlias": "github_ss"
}
```