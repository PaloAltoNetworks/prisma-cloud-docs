Specifies the learning mode for a profile.

To get the `PROFILE_ID` for a profile, follow these steps:

1. Retrieve a list of profiles using the GET method on the `/api/v<VERSION>/profiles/container` endpoint.

2. Copy the value in `_id` to get the `PROFILE_ID` of interest.

## cURL Request

Refer to the following example cURL command that specifies the learning mode for a profile.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"state":"manualLearning"}' \
  https://<CONSOLE>/api/v1/profiles/container/<PROFILE_ID>/learn
```
