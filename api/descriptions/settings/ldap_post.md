Configures the LDAP integration.

The following example curl command enables LDAP integration and specifies the parameters required to integrate with an Active Directory service.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d \
'{
   "enabled": true,
   "url": "ldap://ldapserver.example.com:3268",
   "searchBase": "dc=example,dc=com",
   "accountUpn": "twistlock_service@example.com",
   "accountPassword": {
     "plain": "pass!-W0RD"
   },
   "type": "activedirectory",
   "userSearchIdentifier": "userprincipalname"   
}' \
  https://<CONSOLE>:8083/api/v1/settings/ldap
```
