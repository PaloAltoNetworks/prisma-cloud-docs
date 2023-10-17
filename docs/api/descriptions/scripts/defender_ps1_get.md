Download the Defender set up script for Windows hosts.

Only users that have a user role of Defender Manager or higher (Operator and Administrator) are permitted to download this file.
For more information about each supported role, see
[User roles](https://docs.twistlock.com/docs/latest/access_control/user_roles.html).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  -o defender.ps1 \
  https://<CONSOLE>:8083/api/v1/scripts/defender.ps1
```

NOTE: The downloaded script takes a number of parameters to control how Defender is installed.
To see the default parameters, open Console, go to **Manage > Defenders > Deploy**, and examine how the script is configured based on the options you select.
