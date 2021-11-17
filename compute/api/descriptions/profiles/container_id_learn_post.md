Specify the learning mode for a profile.

To get the `PROFILE_ID` for a profile:

1. Retrieve a list of profiles using the GET method on the `/api/v1/profiles/container` endpoint.

2. For the profile of interest, copy the value in `_id`.
This is the `PROFILE_ID`.

The following example command uses curl and basic auth to specify the learning mode for a profile.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"state":"manualLearning"}' \
  https://<CONSOLE>:8083/api/v1/profiles/container/<PROFILE_ID>/learn
```
