Retrieves all access audits.
Twistlock records access audits every time a Docker Engine or Kubernetes command is run on a host protected by Defender.
You can also configure Twistlock to record audits for any sudo or SSH commands that are executed on hosts protected Defender.

The following example command gives a list of ALL access audits.

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/access
```

To get just the docker audits run it with type=docker parameter. 

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://console:8083/api/v1/audits/access?type=docker

```
