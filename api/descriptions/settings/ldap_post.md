Configures the LDAP integration.

For more information, see [Active Directory](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/active_directory) and [OpenLDAP](https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/authentication/openldap)

## cURL Request

Refer to the following example cURL command that enables the LDAP integration and specifies the parameters required to integrate with an Active Directory service.

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
   "accountUpn": "example_service@example.com",
   "accountPassword": {
     "plain": "pass!-W0RD"
   },
   "type": "activedirectory",
   "userSearchIdentifier": "userprincipalname"   
}' \
  "https://<CONSOLE>/api/v<VERSION>/settings/ldap"
```
