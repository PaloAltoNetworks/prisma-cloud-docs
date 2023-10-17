Returns the LDAP integration settings.

## cURL Request

Refer to the following example cURL request:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  "https://<CONSOLE>/api/v<VERSION>/settings/ldap"
```

## cURL Response

Refer to the following example cURL response:

```bash
$ {
 "enabled": true,
 "url": "ldap://10.176.135.212:379",
 "caCert": "",
 "searchBase": "",
 "groupSearchBase": "ou=Groups,dc=example,dc=org",
 "userSearchBase": "ou=Users,dc=example,dc=org",
 "accountUpn": "cn=admin,dc=example,dc=org",
 "accountPassword": {
   "encrypted": "nkMtVY4NN9RccvbVIfLvJw=="
 },
 "type": "openldap",
 "userSearchIdentifier": "cn"
}
```
