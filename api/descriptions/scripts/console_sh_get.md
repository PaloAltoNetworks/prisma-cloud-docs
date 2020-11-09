Download the Console set up script for Linux hosts.

Only users that have a user role of Defender Manager or higher (Operator and Administrator) are permitted to download this file.
For more information about each supported role, see
[User roles](https://docs.twistlock.com/docs/latest/access_control/user_roles.html).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o console.sh \
  https://<CONSOLE>:8083/api/v1/scripts/console.sh
```

The script must be made executable before it can run:

```bash
$ chmod +x console.sh
```
