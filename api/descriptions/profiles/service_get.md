Retrieves the details and state of all host service runtime models.
The returned JSON object has the following structure:

```  
* service1: model
* service2: model
* service3: model
```

Example curl command:

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X GET \
  https://<CONSOLE>:8083/api/v1/profiles/service
```
