Updates the parameters that define a given collection.

The following example curl command updates the parameters that define the collection named `finance_group_app`.
In general, all parameters in your PUT request should be defined or redefined.
Any field left unspecified is assigned the value of `""` (i.e. an emtpy string).

```bash
$ curl -k \
  -u <USER> \
  -H 'Content-Type: application/json' \
  -X PUT \
  -d \
'{
   "name": "finance_group_app",
   "color": "#ff0000",
   "description": "A super cool collection",
   "images": [
     "docker.io/library/hello-world:latest",
     "docker.io/library/ian_app:1.0"
   ],
   "hosts": [
     "*"
   ]
 }' \
  https://<CONSOLE>:8083/api/v1/collections/test_collection
```
