Returns an array of strings containing VM image names.


### cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -X GET \
  -u <USER> \
  -H 'Content-Type: application/json' \
  "https://<CONSOLE>/api/v<VERSION>/vms/names"
```

### cURL Response

Refer to the following example response:

```
[
  "new-auto-images-cen7-dock",
  "ubuntu-pro-2004-focal-v20210720",
  "user-encrypted2",
  "ubuntu-20.04-lts:1.0.0",
  "user-test-b",
  "user-ubuntu-image-scan1",
  "Canonical:0001-com-ubuntu-server-focal:20_04-lts:20.04.202110260",
  "ubuntu-20.04-lts"
]

```