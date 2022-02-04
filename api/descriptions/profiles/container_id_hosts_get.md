Returns the host/hosts where the container is running.

To get the `PROFILE_ID` for a profile, follow these steps:

1. Retrieve a list of profiles using the GET method on the `/api/v<VERSION>/profiles/container` endpoint.

2. Copy the value in `_id` to get the `PROFILE_ID` of interest.

## cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v1/profiles/container/<PROFILE_ID>/hosts
```
