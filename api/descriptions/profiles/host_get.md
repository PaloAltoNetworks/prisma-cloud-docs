Retrieves the details and state of each host service runtime model on a host-by-host basis.
The returned JSON object has the following structure:

```
* host1:
  * service1: model
  * service2: model
* host2:
  * service1: model
  * service3: model
```

## cURL Request

Refer to the following example cURL command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>/api/v<VERSION>/profiles/host
```
