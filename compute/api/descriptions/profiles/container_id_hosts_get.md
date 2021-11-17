Return the host/hosts where this container is running.

To get the `PROFILE_ID` for a profile:

1. Retrieve a list of profiles using the GET method on the `/api/v1/profiles/container` endpoint.

2. For the profile of interest, copy the value in `_id`.
This is the `PROFILE_ID`.

The following example command uses curl and basic auth to specify the learning mode for a profile.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/profiles/container/<PROFILE_ID>/hosts
```
